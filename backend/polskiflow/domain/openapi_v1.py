"""Static, deterministic API v1 description for separate clients."""


def build_openapi_v1():
    error_response = {
        "description": "Request failed",
        "content": {
            "application/json": {"schema": {"$ref": "#/components/schemas/ErrorEnvelope"}}
        },
    }
    private_errors = {str(code): error_response for code in (401, 405, 503)}
    return {
        "openapi": "3.1.0",
        "info": {
            "title": "PolskiFlow API",
            "version": "1.0.0",
            "description": (
                "Versioned contracts for the PolskiFlow curriculum and learner-owned state. "
                "Curriculum levels are targets, not official CEFR certification."
            ),
        },
        "servers": [{"url": "/", "description": "Same-origin deployment"}],
        "paths": {
            "/api/v1/catalog/": {
                "get": {
                    "operationId": "getCatalog",
                    "summary": "Get the public active course catalog",
                    "responses": {"200": _json_response("Public course catalog")},
                }
            },
            "/api/v1/me/progress/": {
                "get": {
                    "operationId": "getLearnerProgress",
                    "summary": "Get aggregate progress for the authenticated learner",
                    "security": [{"supabaseBearer": []}, {"browserSession": []}],
                    "responses": {"200": _json_response("Owner-scoped progress"), **private_errors},
                }
            },
            "/api/v1/me/history/": {
                "get": {
                    "operationId": "getLearnerHistory",
                    "summary": "Get a paginated owner-scoped lesson completion history",
                    "security": [{"supabaseBearer": []}],
                    "parameters": [
                        {"name": "page", "in": "query", "schema": {"type": "integer", "minimum": 1, "maximum": 500, "default": 1}},
                        {"name": "period", "in": "query", "schema": {"type": "string", "enum": ["7", "30", "90", "all"], "default": "30"}},
                    ],
                    "responses": {"200": _json_response("Owner-scoped lesson history"), **{str(code): error_response for code in (400, 401, 405, 503)}},
                }
            },
            "/api/v1/me/sm2/": {
                "get": {
                    "operationId": "getLearnerSm2",
                    "summary": "Get the learner's personal SM-2 queue",
                    "security": [{"supabaseBearer": []}, {"browserSession": []}],
                    "responses": {"200": _json_response("Owner-scoped SM-2 queue"), **private_errors},
                }
            },
            "/api/v1/me/reading-bookmarks/": {"get": {"operationId": "getReadingBookmarks", "summary": "Get saved reading text IDs", "security": [{"supabaseBearer": []}, {"browserSession": []}], "responses": {"200": _json_response("Owner-scoped reading bookmarks"), **private_errors}}},
            "/api/v1/me/reading-bookmarks/{text_id}/": {
                "parameters": [{"name": "text_id", "in": "path", "required": True, "schema": {"type": "string", "maxLength": 80}}],
                "put": {"operationId": "saveReadingBookmark", "summary": "Save a reading text", "security": [{"supabaseBearer": []}], "responses": {"200": _json_response("Bookmark saved"), **{str(code): error_response for code in (401, 404, 503)}}},
                "delete": {"operationId": "deleteReadingBookmark", "summary": "Remove a reading text", "security": [{"supabaseBearer": []}], "responses": {"200": _json_response("Bookmark removed"), **{str(code): error_response for code in (401, 404, 503)}}},
            },
            "/api/v1/me/lesson-results/": {
                "post": {
                    "operationId": "postLessonResult",
                    "summary": "Store an idempotent lesson-result event for a native client",
                    "security": [{"supabaseBearer": []}],
                    "requestBody": _lesson_result_body(),
                    "responses": {
                        "200": _json_response("Duplicate event confirmed"),
                        "201": _json_response("Event created"),
                        **{str(code): error_response for code in (400, 401, 404, 409, 413, 415, 503)},
                    },
                }
            },
            "/api/v1/me/lesson-results/session/": {
                "post": {
                    "operationId": "postBrowserLessonResult",
                    "summary": "Store a queued browser result without exposing the HttpOnly token",
                    "security": [{"browserSession": [], "csrfHeader": []}],
                    "requestBody": _lesson_result_body(),
                    "responses": {
                        "200": _json_response("Duplicate event confirmed"),
                        "201": _json_response("Event created"),
                        **{str(code): error_response for code in (400, 401, 403, 404, 409, 413, 415, 503)},
                    },
                }
            },
        },
        "components": {
            "securitySchemes": {
                "supabaseBearer": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                    "description": "Supabase access token; never persist it in an offline event queue.",
                },
                "browserSession": {
                    "type": "apiKey",
                    "in": "cookie",
                    "name": "polskiflow_access_token",
                    "description": "HttpOnly browser session cookie managed by PolskiFlow.",
                },
                "csrfHeader": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "X-CSRFToken",
                },
            },
            "schemas": {
                "LessonResultRequest": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": [
                        "event_id", "lesson_id", "plan_date", "completed_at",
                        "cards_total", "cards_known", "contract_version",
                    ],
                    "properties": {
                        "event_id": {"type": "string", "format": "uuid"},
                        "lesson_id": {"type": "string", "minLength": 1, "maxLength": 100},
                        "plan_date": {"type": "string", "format": "date"},
                        "completed_at": {"type": "string", "format": "date-time"},
                        "cards_total": {"type": "integer", "minimum": 0},
                        "cards_known": {"type": "integer", "minimum": 0},
                        "contract_version": {"type": "string", "const": "1.0"},
                        "client_instance_id": {"type": "string", "maxLength": 100},
                    },
                },
                "ErrorEnvelope": {
                    "type": "object",
                    "required": ["api_version", "error"],
                    "properties": {
                        "api_version": {"type": "string", "const": "v1"},
                        "error": {
                            "type": "object",
                            "required": ["code", "detail"],
                            "properties": {
                                "code": {"type": "string"},
                                "detail": {"type": "string"},
                            },
                        },
                    },
                },
            },
        },
    }


def _json_response(description):
    return {
        "description": description,
        "content": {"application/json": {"schema": {"type": "object"}}},
    }


def _lesson_result_body():
    return {
        "required": True,
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/LessonResultRequest"}
            }
        },
    }
