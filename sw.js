/* nvimq - DevSecOps PWA service worker (GitHub Pages / GitLab Pages) */
const CORE = 'nvimq-core-v2';
const RUNTIME = 'nvimq-runtime-v2';
const PRECACHE = [
  '/',
  '/index.html',
  '/404.html',
  '/manifest.webmanifest',
  '/icon-192.png',
  '/icon-512.png',
  '/apple-touch-icon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CORE).then((cache) => cache.addAll(PRECACHE))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => k !== CORE && k !== RUNTIME)
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  const url = new URL(req.url);

  if (req.method !== 'GET') return;
  if (url.origin !== self.location.origin && !/^https:\/\/(fonts\.(googleapis|gstatic)\.com|api\.qrserver\.com)/.test(url.origin)) return;

  /* SPA fallback: navigation offline -> cached index.html */
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(RUNTIME).then((cache) => cache.put(req, copy));
          return res;
        })
        .catch(() =>
          caches.open(RUNTIME).then((cache) =>
            cache.match(req).then((hit) =>
              hit || caches.open(CORE).then((c) => c.match('/index.html'))
            )
          )
        )
    );
    return;
  }

  /* static same-origin: cache-first, fallback to network */
  if (url.origin === self.location.origin) {
    event.respondWith(
      caches.match(req).then((hit) => {
        if (hit) return hit;
        return fetch(req).then((res) => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(RUNTIME).then((cache) => cache.put(req, copy));
          }
          return res;
        });
      })
    );
    return;
  }

  /* fonts / qr: stale-while-revalidate */
  event.respondWith(
    caches.match(req).then((hit) => {
      const net = fetch(req).then((res) => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(RUNTIME).then((cache) => cache.put(req, copy));
        }
        return res;
      }).catch(() => hit);
      return hit || net;
    })
  );
});
