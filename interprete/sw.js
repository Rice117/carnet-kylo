// Interprète KYLO (version site) : marche aussi sans Internet pour les phrases prêtes et les prix.
// Toujours la version la plus récente quand il y a Internet (réseau d'abord), la copie gardée sinon.
// Ne touche qu'aux fichiers de /interprete/ : jamais au carnet KYLO Achats, jamais aux traductions.
const VERSION = 'interprete-kylo-1.1.0-' + "16/10 06:30";
const FICHIERS = ['./', './index.html', './jsQR.js', './icone-180.png'];
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(FICHIERS.map((f) => new Request(f, { cache: 'reload' })))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys()
    .then((noms) => Promise.all(noms.filter((n) => n.startsWith('interprete-kylo-') && n !== VERSION).map((n) => caches.delete(n))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET' || !req.url.startsWith(self.registration.scope)) return;
  e.respondWith(fetch(req).then((rep) => {
    if (rep && rep.ok && rep.type === 'basic') { const copie = rep.clone(); caches.open(VERSION).then((c) => c.put(req, copie)); }
    return rep;
  }).catch(() => caches.open(VERSION).then((c) => c.match(req, { ignoreSearch: true })
    .then((trouve) => trouve || (req.mode === 'navigate' ? c.match('./index.html') : Response.error())))));
});
