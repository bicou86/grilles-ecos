var CACHE_NAME = 'ecos-v5';
var APP_SHELL = [
  '/',
  '/index.html',
  '/exam.html',
  '/cases/scoring.js',
  '/cases/persistence.js',
  '/cases/srs.js',
  '/cases/case-styles.css',
  '/simulation/launcher.html',
  '/simulation/transcript.html',
  '/report/viewer.html',
  '/js/simulation.js',
  '/js/transcript.js',
  '/js/report.js'
];

// Install: cache app shell
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(APP_SHELL);
    }).then(function() {
      return self.skipWaiting();
    })
  );
});

// Activate: clean old caches
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(names) {
      return Promise.all(
        names.filter(function(name) { return name !== CACHE_NAME; })
             .map(function(name) { return caches.delete(name); })
      );
    }).then(function() {
      return self.clients.claim();
    })
  );
});

// Fetch: network-first for app shell, cache-first for case files and static assets
self.addEventListener('fetch', function(event) {
  var url = new URL(event.request.url);

  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  // Case HTML files and CSS: cache-first (lazy cache on first access)
  if (url.origin === location.origin && url.pathname.match(/\/cases\/.*\.(html|css)$/)) {
    event.respondWith(
      caches.match(event.request).then(function(cached) {
        if (cached) return cached;
        return fetch(event.request).then(function(response) {
          if (response.ok) {
            var clone = response.clone();
            caches.open(CACHE_NAME).then(function(cache) { cache.put(event.request, clone); });
          }
          return response;
        });
      })
    );
    return;
  }

  // App shell files: network-first
  if (url.origin === location.origin && (url.pathname === '/' || url.pathname.endsWith('.html') || url.pathname.endsWith('.js'))) {
    event.respondWith(
      fetch(event.request).then(function(response) {
        if (response.ok) {
          var clone = response.clone();
          caches.open(CACHE_NAME).then(function(cache) { cache.put(event.request, clone); });
        }
        return response;
      }).catch(function() {
        return caches.match(event.request);
      })
    );
    return;
  }

  // CDN assets (Chart.js, fonts): cache-first
  if (url.hostname !== location.hostname) {
    event.respondWith(
      caches.match(event.request).then(function(cached) {
        if (cached) return cached;
        return fetch(event.request).then(function(response) {
          if (response.ok) {
            var clone = response.clone();
            caches.open(CACHE_NAME).then(function(cache) { cache.put(event.request, clone); });
          }
          return response;
        });
      })
    );
    return;
  }
});

// Message handler for bulk cache of case files
self.addEventListener('message', function(event) {
  if (event.data && event.data.type === 'CACHE_CASES') {
    var urls = event.data.urls || [];
    caches.open(CACHE_NAME).then(function(cache) {
      var total = urls.length;
      var done = 0;
      urls.forEach(function(url) {
        cache.match(url).then(function(existing) {
          if (existing) {
            done++;
            notifyProgress(done, total);
            return;
          }
          fetch(url).then(function(response) {
            if (response.ok) cache.put(url, response);
            done++;
            notifyProgress(done, total);
          }).catch(function() {
            done++;
            notifyProgress(done, total);
          });
        });
      });
    });
  }
});

function notifyProgress(done, total) {
  self.clients.matchAll().then(function(clients) {
    clients.forEach(function(client) {
      client.postMessage({ type: 'CACHE_PROGRESS', done: done, total: total });
    });
  });
}
