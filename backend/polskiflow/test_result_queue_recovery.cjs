"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");

function request(run) {
  const result = {};
  queueMicrotask(() => {
    try { result.result = run(); result.onsuccess?.(); }
    catch (error) { result.error = error; result.onerror?.(); }
  });
  return result;
}

function fakeIndexedDB() {
  const rows = new Map();
  const store = {
    createIndex() {},
    get(key) { return request(() => rows.get(key)); },
    put(item) { return request(() => { rows.set(item.key, structuredClone(item)); return item.key; }); },
    delete(key) { return request(() => rows.delete(key)); },
    index() {
      return {
        getAll(range) {
          return request(() => [...rows.values()].filter((item) => item.namespace === range.lower[0]));
        },
      };
    },
  };
  const database = {
    createObjectStore() { return store; },
    transaction() { return { objectStore() { return store; } }; },
    close() {},
  };
  return {
    open() {
      const result = {};
      queueMicrotask(() => {
        result.result = database;
        result.onupgradeneeded?.();
        result.onsuccess?.();
      });
      return result;
    },
  };
}

global.IDBKeyRange = { bound(lower, upper) { return { lower, upper }; } };
const queueModule = require(path.join(__dirname, "learning/static/polskiflow/result-queue.js"));

(async () => {
  const calls = [];
  let online = false;
  const queue = queueModule.createQueue({
    indexedDB: fakeIndexedDB(),
    fetch: async (url, options) => {
      calls.push({ url, options });
      if (!online) throw new TypeError("network unavailable");
      const eventId = JSON.parse(options.body).event_id;
      return { status: 201, json: async () => ({ data: { event_id: eventId } }) };
    },
  });
  const namespace = "opaque-browser-namespace";
  const payload = {
    event_id: "event-offline-online",
    lesson_id: "a1-words",
    plan_date: "2026-09-14",
    completed_at: "2026-09-14T08:00:00Z",
    cards_total: 8,
    cards_known: 7,
    contract_version: 1,
  };

  await queue.enqueue(namespace, payload);
  payload.cards_known = 0;
  const offlineResult = await queue.flushSession(namespace, "csrf-test-value");
  assert.deepEqual(offlineResult, { sent: 0, pending: 1, authRequired: false });
  const queued = await queue.list(namespace);
  assert.equal(queued.length, 1);
  assert.equal(queued[0].payload.cards_known, 7, "persisted payload must be immutable");

  online = true;
  const recovered = await queue.flushSession(namespace, "csrf-test-value");
  assert.deepEqual(recovered, { sent: 1, pending: 0, authRequired: false });
  assert.equal((await queue.list(namespace)).length, 0, "matching confirmation removes event");

  const sent = calls.at(-1);
  assert.equal(sent.url, "/api/v1/me/lesson-results/session/");
  assert.equal(sent.options.credentials, "same-origin");
  assert.equal(sent.options.headers.Authorization, undefined);
  assert.equal(sent.options.headers["X-CSRFToken"], "csrf-test-value");
  const serialized = JSON.stringify(sent);
  for (const secret of ["access_token", "refresh_token", "user_id", "email"]) {
    assert.equal(serialized.includes(secret), false, `request leaked ${secret}`);
  }
})().catch((error) => { console.error(error); process.exitCode = 1; });
