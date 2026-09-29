// KYLO Achats - carnet de voyage : ce qui le fait marcher SANS INTERNET (28/09/2026).
// A la premiere ouverture (avec Internet), il range le carnet entier dans l'appareil.
// Ensuite, chaque ouverture se sert dans ce rangement : l'avion, la Chine, sans reseau.
// Une nouvelle version change le nom VERSION : l'appareil la range a la prochaine
// ouverture avec Internet, puis jette l'ancienne. Les achats, eux, ne sont jamais ici :
// ils restent dans la memoire du carnet et dans votre fichier.
const VERSION = 'carnet-kylo-1.0.2-10b425c755';
const FICHIERS = ["./","./index.html","./manifest.webmanifest","./lecteur-codes.js","./icones/icone-180.png","./icones/icone-192.png","./icones/icone-512-masquable.png","./icones/icone-512.png"];

self.addEventListener('install', (e) => {
  // cache: 'reload' : on va chercher les fichiers NEUFS sur Internet, jamais une vieille copie
  // gardee par le navigateur (sinon une nouvelle version pourrait ranger l'ancienne page).
  e.waitUntil(caches.open(VERSION)
    .then((c) => c.addAll(FICHIERS.map((f) => new Request(f, { cache: 'reload' }))))
    .then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys()
    .then((noms) => Promise.all(noms.filter((n) => n.startsWith('carnet-kylo-') && n !== VERSION).map((n) => caches.delete(n))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET' || !req.url.startsWith(self.registration.scope)) return;
  e.respondWith(caches.open(VERSION).then((c) => c.match(req, { ignoreSearch: true }).then((trouve) => {
    if (trouve) return trouve;
    return fetch(req).then((rep) => {
      if (rep && rep.ok && rep.type === 'basic') c.put(req, rep.clone());
      return rep;
    }).catch(() => (req.mode === 'navigate' ? c.match('./index.html') : Response.error()));
  })));
});
