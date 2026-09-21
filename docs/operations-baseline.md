# Production operations baseline

PolskiFlow provides two unauthenticated, privacy-safe probes:

- `GET /health/` is a liveness check. It only confirms that Django can respond and
  never calls the database or Supabase Auth.
- `GET /ready/` checks the default database with `SELECT 1`. On Vercel it also
  confirms that the required Supabase variables are present. It returns HTTP 503
  when the application should not receive traffic.

Both responses use `Cache-Control: no-store` and expose only component states,
never exception messages, connection strings, keys, versions, or user data.

Every response receives an `X-Request-ID`. HTTP 5xx responses, uncaught
exceptions, and slow requests are written to the platform log as structured
`key=value` events. Logs contain method, path without query parameters, status,
duration, and request ID; they do not contain bodies, cookies, email addresses,
tokens, IP addresses, or exception messages. Exception logs expose only the
exception class. `REQUEST_SLOW_THRESHOLD_MS` defaults to 1500 ms.

Minimal production checks:

```shell
curl --fail --max-time 10 https://polish-learn.vercel.app/health/
curl --fail --max-time 10 https://polish-learn.vercel.app/ready/
```

Use the returned `X-Request-ID` to correlate a failed client request with Vercel
runtime logs. These probes do not replace synthetic user-flow monitoring,
database backups, or alerts.
