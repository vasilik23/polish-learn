/* Offline result queue prototype. Not loaded by the Django UI: its Supabase
 * tokens remain HttpOnly and must only be supplied by a client at flush time. */
(function (root, factory) {
  "use strict";
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.PolskiFlowResultQueue = api;
}(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";
  const DATABASE = "polskiflow-result-queue";
  const STORE = "events";
  const MAX_ATTEMPTS = 5;

  function namespace(userId) {
    if (!userId || typeof userId !== "string") throw new Error("userId is required");
    return `user:${userId}`;
  }
  function validatePayload(payload) {
    const required = ["event_id", "lesson_id", "plan_date", "completed_at", "cards_total", "cards_known", "contract_version"];
    if (!payload || typeof payload !== "object" || required.some((key) => !(key in payload))) throw new Error("Incomplete lesson-result payload");
    const forbidden = ["access_token", "refresh_token", "token", "email", "user_id"];
    if (forbidden.some((key) => key in payload)) throw new Error("Sensitive queue field");
  }
  function openDatabase(indexedDBImpl) {
    return new Promise((resolve, reject) => {
      const request = indexedDBImpl.open(DATABASE, 1);
      request.onupgradeneeded = () => {
        const store = request.result.createObjectStore(STORE, { keyPath: "key" });
        store.createIndex("namespace_created", ["namespace", "createdAt"]);
      };
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }
  function requestResult(request) {
    return new Promise((resolve, reject) => {
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }
  function createQueue(options) {
    const indexedDBImpl = options?.indexedDB || globalThis.indexedDB;
    const fetchImpl = options?.fetch || globalThis.fetch;
    const wait = options?.wait || ((ms) => new Promise((resolve) => setTimeout(resolve, ms)));
    const onStatus = options?.onStatus || function () {};
    if (!indexedDBImpl) throw new Error("IndexedDB is unavailable");
    async function transaction(mode, operation) {
      const database = await openDatabase(indexedDBImpl);
      try { return await operation(database.transaction(STORE, mode).objectStore(STORE)); }
      finally { database.close(); }
    }
    async function enqueue(userId, payload) {
      validatePayload(payload);
      const owner = namespace(userId);
      const item = { key: `${owner}:${payload.event_id}`, namespace: owner, createdAt: Date.now(), attempts: 0, state: "pending", payload: JSON.parse(JSON.stringify(payload)) };
      const existing = await transaction("readonly", (store) => requestResult(store.get(item.key)));
      if (existing) {
        if (JSON.stringify(existing.payload) !== JSON.stringify(item.payload)) throw new Error("Idempotency conflict");
        return existing.key;
      }
      await transaction("readwrite", (store) => requestResult(store.put(item)));
      onStatus({ state: "queued", eventId: payload.event_id });
      return item.key;
    }
    async function list(userId) {
      const owner = namespace(userId);
      const items = await transaction("readonly", (store) => requestResult(store.index("namespace_created").getAll(IDBKeyRange.bound([owner, 0], [owner, Number.MAX_SAFE_INTEGER]))));
      return items.sort((a, b) => a.createdAt - b.createdAt);
    }
    async function remove(key) { await transaction("readwrite", (store) => requestResult(store.delete(key))); }
    async function save(item) { await transaction("readwrite", (store) => requestResult(store.put(item))); }
    async function flush(userId, accessToken) {
      if (!accessToken || typeof accessToken !== "string") {
        onStatus({ state: "auth-required" });
        return { sent: 0, pending: (await list(userId)).length, authRequired: true };
      }
      let sent = 0;
      for (const item of await list(userId)) {
        if (item.state === "needs-attention") continue;
        let resolved = false;
        while (!resolved && item.attempts < MAX_ATTEMPTS) {
          let response = null;
          try {
            response = await fetchImpl("/api/v1/me/lesson-results/", { method: "POST", credentials: "same-origin", headers: { "Authorization": `Bearer ${accessToken}`, "Content-Type": "application/json" }, body: JSON.stringify(item.payload) });
          } catch (error) { /* Offline: keep the immutable payload queued. */ }
          if (response && (response.status === 200 || response.status === 201)) {
            const body = await response.json().catch(() => null);
            if (body?.data?.event_id === item.payload.event_id) {
              await remove(item.key); sent += 1; resolved = true;
              onStatus({ state: "sent", eventId: item.payload.event_id });
              continue;
            }
          }
          if (response?.status === 401) {
            onStatus({ state: "auth-required", eventId: item.payload.event_id });
            return { sent, pending: (await list(userId)).length, authRequired: true };
          }
          if (response && response.status >= 400 && response.status < 500) {
            item.state = "needs-attention"; await save(item); resolved = true;
            onStatus({ state: "needs-attention", eventId: item.payload.event_id, status: response.status });
            continue;
          }
          item.attempts += 1; await save(item);
          if (item.attempts >= MAX_ATTEMPTS) {
            onStatus({ state: "retry-paused", eventId: item.payload.event_id });
            continue;
          }
          await wait(Math.min(1000 * (2 ** (item.attempts - 1)), 16000));
        }
      }
      const pending = (await list(userId)).length;
      onStatus({ state: pending ? "pending" : "synced", pending });
      return { sent, pending, authRequired: false };
    }
    return { enqueue, list, remove, flush };
  }
  return { createQueue, validatePayload, constants: { DATABASE, STORE, MAX_ATTEMPTS } };
}));
