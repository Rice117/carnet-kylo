// KYLO Achats - carnet de voyage : ce qui le fait marcher SANS INTERNET (28/09/2026).
// A la premiere ouverture (avec Internet), il range le carnet entier dans l'appareil.
// Ensuite, chaque ouverture se sert dans ce rangement : l'avion, la Chine, sans reseau.
// Une nouvelle version change le nom VERSION : l'appareil la range a la prochaine
// ouverture avec Internet, puis jette l'ancienne. Les achats, eux, ne sont jamais ici :
// ils restent dans la memoire du carnet et dans votre fichier.
const VERSION = 'carnet-kylo-1.0.3-66067c331a';
const FICHIERS = ["./","./index.html","./manifest.webmanifest","./lecteur-codes.js","./icones/icone-180.png","./icones/icone-192.png","./icones/icone-512-masquable.png","./icones/icone-512.png"];
// L'empreinte exacte (SHA-256) de chaque fichier de CETTE version. 1.0.3 : si Internet donne un
// fichier different (copie en retard chez l'hebergeur, fichier d'une autre fabrication), on ne
// range RIEN sous le nom de cette version : l'ancienne version reste en place, intacte, et on
// reessaiera a la prochaine ouverture avec Internet.
const EMPREINTES = {"./":"922499e74cc1cb8d75860010ea1d91b1167d0b006f9fefd5c422f5750b31ece2","./index.html":"922499e74cc1cb8d75860010ea1d91b1167d0b006f9fefd5c422f5750b31ece2","./manifest.webmanifest":"206117d1f2fe00f5deb4cbaf42a9ddf61c62f4d7d5afa38f7810b28abbfe47eb","./lecteur-codes.js":"3e6840539ee0b66b9d70323bfdb67de1dad7da7d005c7a433c74da29bab2e0ba","./icones/icone-180.png":"ad6843165e8129d65fa23fdcd1a1ae3cc653ca5e6de44f3153aeef797589e510","./icones/icone-192.png":"59d586d2d7cb9c66ca035055a9a1ff71e8260e15a8722624cda9f128d0229bd2","./icones/icone-512-masquable.png":"9bbd5f30c9ac77b48daa6b80f73f33f40b2aba60ec6b49e7102b1f08e7958a85","./icones/icone-512.png":"9339df7ecec70578c8db3084bf5d2ad7a1bc26788793eabd963a387a656def97"};
const hexa = (buf) => Array.from(new Uint8Array(buf)).map((o) => o.toString(16).padStart(2, '0')).join('');

self.addEventListener('install', (e) => {
  // cache: 'reload' : on va chercher les fichiers NEUFS sur Internet, jamais une vieille copie
  // gardee par le navigateur (sinon une nouvelle version pourrait ranger l'ancienne page).
  e.waitUntil(caches.open(VERSION)
    .then((c) => c.addAll(FICHIERS.map((f) => new Request(f, { cache: 'reload' })))
      .then(() => Promise.all(FICHIERS.map((f) => c.match(f)
        .then((r) => (r ? r.arrayBuffer() : new ArrayBuffer(0)))
        .then((b) => crypto.subtle.digest('SHA-256', b))
        .then((h) => hexa(h) === EMPREINTES[f])))))
    .then((bons) => {
      if (bons.every(Boolean)) return self.skipWaiting();
      return caches.delete(VERSION).then(() => { throw new Error('fichiers en retard sur la version ' + VERSION); });
    }));
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
