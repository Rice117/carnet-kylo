# KYLO Achats — carnet de voyage

Le carnet d'achats de KYLO EURGUINE, en application pour téléphone et ordinateur.

- Il s'installe sur l'écran d'accueil et marche **sans Internet** (en Chine, dans l'avion).
- Ce dépôt contient **uniquement le programme** : aucune donnée, aucun prix, aucun achat.
  Les achats restent dans l'appareil de celui qui s'en sert, et dans son fichier `.json`.
- Ce programme est fabriqué à partir du carnet du magasin (`KYLO-Achats.html`) par l'outil
  `construire.js`. Ne pas le modifier à la main : refaire une version.

Version 1.0.3 — 02/10/2026 (mémoire pleine : plus aucun achat perdu en silence ; corrections des deux vérifications indépendantes).

Version 1.2.0 — 19/10/2026 : **Au marché**. Bouton vert 📷 Marché : photo du produit (et du prix), prix dit par
le vendeur dans sa devise (¥ par défaut) avec les francs guinéens et les euros tout de suite, minimum de commande,
notes ; QR WeChat ou carte de visite (vCard) lus par le carnet et gardés en image ; tout se range dans Comparer
(une offre par prix, avec photo) et dans « Fournisseurs rencontrés » (code F01…, ✅ à contacter / 🤔 peut-être / ❌ non,
ajout sur WeChat). Fiche Achat : les francs sous le prix. Reprise des fiches de l'Interprète. Rien de retiré.
⚠ Retouche faite directement sur ce fichier (l'ordinateur du magasin n'était pas joignable) : à reporter dans
`KYLO-Achats.html` avant la prochaine fabrication par `construire.js`, sinon elle serait perdue.

## fiche.html — page d'aide de l'Interprète KYLO (16/10/2026)

Met une fiche fournisseur dans les Contacts de l'iPhone et lance l'appel. Elle ne garde rien
et n'envoie rien : la fiche voyage dans le lien, après le `#`, que le navigateur n'envoie jamais à
Internet. Elle ne touche pas au carnet (aucun fichier du carnet modifié).

## interprete/ — l'Interprète KYLO, version site (16/10/2026)

Traduction parlée (micro direct dans Safari), mode Réunion, phrases prêtes, fiches fournisseurs par QR code,
calcul des prix. Fabriqué par `build.js` du projet Interprète : ne pas modifier à la main.
Son propre service worker (portée `interprete/`) ; ne touche à aucun fichier du carnet.
