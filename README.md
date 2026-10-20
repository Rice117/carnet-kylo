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

Version 1.3.0 — 20/10/2026 : **Catalogues et demandes de prix**. Fiche complète par fournisseur (« Sa fiche ») :
photo de sa carte (QR lu par le carnet), « Coller le texte de la carte » (Texte en direct de l'iPhone), pages du
catalogue rangées dans la réserve du téléphone (IndexedDB, hors fichier .json), modèles par famille (batterie, carton,
colisage, poids, pièces par conteneur), ⭐ « m'intéresse », prix reçus tout de suite en francs ; demande de prix et
relance en anglais + chinois (WeChat, e-mail, WhatsApp) ; « Comparer les prix par produit » tous fournisseurs confondus ;
« Ajouter ce que Claude a lu » (code KYLOZ:/KYLO1: collé, fichier, ou lien #kylo=… qui ne part jamais sur Internet).
Rien de retiré. ⚠ Même remarque que la 1.2.0 : à reporter dans `KYLO-Achats.html` (module `catalogues-1.3.0.html`).

Version 1.4.0 — 20/10/2026 : **Sur le terrain**. Onglet 🏭 Fournisseurs en tête (le carnet s'y ouvre) ; ⚡ Scanner un
stand (caméra dans le carnet : carte recto-verso, catalogue, produit, panneau — tout rangé chez le même fournisseur) ;
lecture des cartes SANS Internet (dossier `ocr/`, Tesseract.js, téléchargé une fois dans le rangement « kylo-ocr-1 ») :
tous les QR (WeChat et WhatsApp), portable, e-mail, société, contact, marqués « à vérifier » ; un fournisseur déjà connu
est reconnu (pas de doublon) ; 📚 Ranger une pile de photos (cartes et pages triées par fournisseur, aperçu corrigeable,
📥 à ranger) ; produits en photo (grille), fichier de Claude avec la photo de chaque produit ; ✉️ demande de prix par
images numérotées + message en chinois ; 💬 la réponse collée place chaque prix sur son produit ; 🀄 questions au vendeur
en chinois par famille (réponses relues en français, prix au stand) ; ✂️ découper au doigt un bloc de produits ;
l'en-tête ne colle plus en haut. Rien de retiré. ⚠ Même remarque : à reporter dans `KYLO-Achats.html`
(modules `terrain-1.4.0.html`, `produits-1.4.0.html`, `vendeur-1.4.0.html`, et la ligne `/ocr/` du service worker).

Version 1.5.0 — 20/10/2026 : **Fichiers WeChat et gammes**. 📥 « Fichier reçu sur WeChat » (Fournisseurs et fiche
du fournisseur) : un catalogue PDF est lu dans le téléphone (texte réel du PDF, sans Internet) — chaque modèle avec sa
photo découpée, sa référence, ses caractéristiques traduites, son carton ; les coordonnées remplissent la fiche ; un
fournisseur connu est reconnu, sinon il est créé ; une liste de prix Excel ou PDF (型号 / 单价 / 起订量 / 装箱…) pose les
prix sur les produits, par gamme (一档, 二档…) ou par quantité ; une capture d'écran de prix est lue ; un PDF fait de
photos est gardé en pages. Aperçu avant de ranger ; le fichier d'origine reste sur la fiche (📤 Envoyer). Demande de prix :
le prix de chaque gamme et les questions en chinois (A, B, C…) partent avec les images ; la réponse « A = 工厂 » est relue
en français. Gammes partout (fiche, Comparer par produit, vendeur au stand : 1 à 4 gammes). Rien de retiré.
⚠ Même remarque : à reporter dans `KYLO-Achats.html` (modules `terrain-1.5.0.html`, `produits-1.5.0.html`,
`vendeur-1.5.0.html`, `fichiers-1.5.0.html`).

Version 1.5.1 — 20/10/2026 : **PDF aux lettres dessinées, « À qui ? »**. Un catalogue PDF dont les lettres sont dessinées
(fait dans Illustrator : aucun texte dans le fichier) est lu page par page dans le téléphone : photos de produits détourées
(transparence du PDF, photos cachées écartées), lettres lues sur l'image (et à part sur les barres de couleur : rangées
« ITEM NO », étiquettes des grilles d'accessoires), références redressées par leurs voisines, famille d'après le titre de la page ;
tout est marqué « à vérifier ». Familles d'aspirateurs ; questions « aspirateurs » en chinois. Avant d'ouvrir WeChat, l'écran
« À qui envoyez-vous ? » (code du fournisseur en grand, nom chinois, photo de sa carte ; nom à mettre en « Remarque » dans WeChat ;
dans WeChat : 🔍 → code). Un fichier de Claude qui porte le code du fournisseur va chez lui. Rien de retiré.
⚠ Même remarque : à reporter dans `KYLO-Achats.html` (modules `terrain-1.5.1.html`, `produits-1.5.1.html`, `vendeur-1.5.1.html`,
`fichiers-1.5.1.html`, et les retouches de `construire-1.5.1.py`).

## ocr/ — la lecture du texte sans Internet (1.4.0) et des fichiers WeChat (1.5.0)

Fichiers de tesseract.js 5.1.1 et deux langues (anglais, chinois simplifié), sans modification, licence Apache 2.0
(voir `ocr/LICENCES.txt`). Le service worker du carnet ne les recopie pas : le carnet les range une fois à part.
1.5.0 : PDF.js 3.11.174 (Apache 2.0) avec 20 tables de caractères chinois (Adobe, BSD) et SheetJS 0.18.5 (Apache 2.0),
sans modification, rangés de la même façon.

## fiche.html — page d'aide de l'Interprète KYLO (16/10/2026)

Met une fiche fournisseur dans les Contacts de l'iPhone et lance l'appel. Elle ne garde rien
et n'envoie rien : la fiche voyage dans le lien, après le `#`, que le navigateur n'envoie jamais à
Internet. Elle ne touche pas au carnet (aucun fichier du carnet modifié).

## interprete/ — l'Interprète KYLO, version site (16/10/2026)

Traduction parlée (micro direct dans Safari), mode Réunion, phrases prêtes, fiches fournisseurs par QR code,
calcul des prix. Fabriqué par `build.js` du projet Interprète : ne pas modifier à la main.
Son propre service worker (portée `interprete/`) ; ne touche à aucun fichier du carnet.
