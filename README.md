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

Version 1.5.2 — 20/10/2026 : **Une seule fiche, bien rangée**. La photo de la carte (fiche Marché, ✏️ Modifier, Sa fiche)
remplit les cases sous les yeux (nom affiché, société, contact, portable, WeChat, e-mail ; en vert = à vérifier) et la carte
est gardée dans la fiche, relisible. Les mêmes cases dans la fiche Marché, ✏️ Modifier et Sa fiche ; le portable est une seule
case partout. « 🧹 Mettre de l'ordre » (fait seul une fois) : cartes du Marché rangées et relues, portable accordé, nom
« Marque — Prénom » quand il n'a pas été tapé. Doublons proposés (« Réunir » / « Ce sont deux fournisseurs »). « 📋 Où j'en
suis » : chaque fournisseur, ce qui est fait et le bouton de la prochaine étape (carte, catalogue, prix). « 📖 Demander son
catalogue » (chinois puis anglais). « 📤 Envoyer à Claude » : fiches et cartes dans un fichier ; le retour de Claude corrige
les cases lues par le téléphone, jamais celles tapées. Lecture des cartes : le contact est la personne (pas une fin de nom
de société), lettres écartées recollées, e-mail coupé recollé. Rien de retiré.
⚠ Même remarque : à reporter dans `KYLO-Achats.html` (module `fiche-1.5.2.html` et les retouches de `construire-1.5.2.py`).

Version 1.6.0 — 21/10/2026 : **Au stand, tout au même endroit**. Un seul écran « 📷 Au stand » (le bouton vert 📷, Fournisseurs,
Sa fiche et Comparer y mènent) : 1. sa carte de visite, face 1 et face 2 dans la MÊME fiche, les cases se remplissent seules
(en vert : à vérifier) ; 2. ses QR WeChat et WhatsApp, chacun à sa place (l'un n'efface plus l'autre ; un QR montré dans la
mauvaise case va à la bonne ; l'autre QR déjà gardé est ignoré) ; 3. ses produits : photo, prix → francs guinéens ET euros tout
de suite, quantité, « Ajouter » (rien n'est perdu en passant au stand suivant) ; 4. catalogue et panneau en rafale ; 5. notes.
L'appareil photo du carnet montre un cadre blanc et ne garde que le cadre (la plus nette de 4 images). La même personne déjà
dans le carnet : « Réunir » en un appui. Le carnet refermé par le téléphone revient au même stand avec le produit commencé.
Lecture des cartes : agrandie, tournée, redressée, rognée autour du texte ou du QR, inversée si la carte est foncée ; étiquettes
chinoises et anglaises (手机, 微信, WhatsApp, Mob, Name…) ; deux QR côte à côte lus tous les deux. En tête de chaque fournisseur :
la photo de son produit. Sa fiche : « Vus au stand : ses prix » (francs et euros) ; toucher une carte → « Relire la carte ».
À la première ouverture, les cartes des fiches incomplètes sont relues (seules les cases vides se remplissent). Rien de retiré.
⚠ Même remarque : à reporter dans `KYLO-Achats.html` (module `stand-1.6.0.html` et les retouches de `construire-1.6.0.py`).

Version 1.6.1 — 21/10/2026 : **Envoyer à Claude, mémoire allégée, classement**. « 📤 Envoyer à Claude » (Fournisseurs →
📋 Où j'en suis) prépare un ou plusieurs fichiers ZIP de moins de 16 Mo : les fiches (fiches.json) et les photos à part
(cartes face 1 et 2, produits vus au stand, pages, panneaux), un bouton par partie. La mémoire du carnet (5 Mo) ne garde plus
les images : elles sont rangées dans la réserve des photos du téléphone et reviennent à l'ouverture (« mémoire pleine » réglé,
rien de perdu ; la sauvegarde garde les images). Le retour de Claude (format kylo-import) peut porter un « classement » :
catégorie, groupe de produits, note de fiabilité 0–5 avec ses raisons et ses sources ; Fournisseurs « 📂 Par catégorie »
(du mieux noté au moins bien noté) ; Sa fiche « 🔎 Qui est-ce ? Fiabilité ». Rien de retiré.
⚠ Même remarque : à reporter dans `KYLO-Achats.html` (module `classement-1.6.1.html` et les retouches de `construire-1.6.1.py`).

Version 1.7.0 — 21/10/2026 : **Des prix à l'achat, et le contrat**. Sa fiche → « 💰 Demander ses prix » : les produits vus
au stand et ceux du catalogue, numérotés ; prix en yuans, quantité minimum, prix pour 2 ou 3 quantités, en 3 qualités
(高档 / 中档 / 低档) et leur différence ; envoyés en photos numérotées, en tableau Excel à remplir (feuille cachée « kylo »)
et en message chinois-anglais. Le tableau rempli revient par « 📥 Fichier reçu sur WeChat » et chaque prix va sur le bon
produit ; le retour de Claude (format kylo-import) peut porter des « offres » (3 qualités, paliers, prix à proposer) et
le « marché » guinéen (prix de vente, frais jusqu'au magasin). Sur chaque produit : le tableau des qualités en ¥, francs et
dollars, « ⛔ Ne payez pas plus de » (prix de vente × (1 − marge) ÷ (1 + frais)), « 🎯 Proposez ». « 🛒 J'achète » : la
qualité et la quantité donnent le prix de cette quantité, le total, le budget ; « Mes achats décidés » et l'objectif de
30 à 35 produits différents. Négocier s'ouvre rempli et compte la marge comme Comparer. « 📝 Contrat d'achat » : un PDF
chinois-anglais (et une version française) rempli avec les achats chez ce fournisseur — acompte, contrôle avant le solde,
remplacement ou remboursement, délai et pénalités, compte bancaire de la société seulement — fait dans le téléphone.
Les dollars à côté des euros ; plus aucune écriture sous 14 px. Rien de retiré.
Aussi dans la 1.7.0 : les frais jusqu'au magasin se comptent au VOLUME (bateau = m³ par pièce × prix du m³, douane sur la
valeur arrivée, + 5 %) ; « 💬 L'ajouter sur WeChat » (WeChat ne permet à aucune application d'ouvrir un profil ou d'envoyer
une invitation : le carnet prépare le QR dans Photos, l'ID ou le portable copié, le mot d'invitation chinois, puis suit
« ⏳ invitation envoyée » → « 🤝 accepté » → demande de catalogue) ; les grands catalogues (des milliers de modèles, chacun
avec sa photo) : familles repliées dessinées à l'ouverture, en Photos comme en Détails et dans Comparer par produit (60
lignes à la fois) ; la mémoire du téléphone n'écrit pas les cases vides des produits (completerCarnet les remet à
l'ouverture) ; un fichier kylo-import peut arriver en plusieurs parties, la suite d'un fournisseur se range chez lui.
⚠ Même remarque : à reporter dans `KYLO-Achats.html` (modules `prix-1.7.0.html`, `contrat-1.7.0.html`, `wechat-1.7.0.html` et les retouches de `construire-1.7.0.py`).

Version 1.8.0 — 22/10/2026 : **Tout se parle**. « + Achat » : aide sous « Qté / carton » et « Cartons », calcul en direct
(12 × 50 = 600), le feu 🟢 🟡 🔴 sur le prix (rendu magasin et prix maximum, calculés avec le DEUXIÈME prix = prix affiché
− écart de marchandage réglable, le bateau au volume, la douane), le fournisseur choisi dans le carnet (créé s'il manque),
bannière des codes-barres claire. Comparer → achat garde fournisseur, photo et notes. Négocier : « Avec quel fournisseur ? »,
« 🤝 Négocier avec lui » depuis Sa fiche (pré-rempli). Les bonnes questions : chaque question en chinois, 是 / 否 / autre +
« ma condition », écran à tendre au vendeur, message chinois + anglais. Sa fiche : questions, réponses, conditions,
négociations, achats. Module `coherence-1.8.0.html`, `construire-1.8.0.py` (part de la 1.7.0). Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.9.0 — 23/10/2026 : **Les choix de Claude**. Nouvel onglet « ⭐ Choix de Claude » (à la place du Radar, qui reste
ouvrable) : les produits conseillés arrivent par un fichier `KYLO-choix-Claude-….json` (même bouton que les catalogues),
chacun avec sa raison, la quantité de départ, le prix usine estimé et à ne pas dépasser, le rendu magasin, le prix de vente
(2ᵉ prix), la marge, le marché (Guinée, voisins) ; ✅ Je prends / ⏸ Plus tard / ❌ Écarter, ma quantité, ma note, le budget
qui se remplit ; une nouvelle liste met le texte à jour sans toucher aux décisions (les produits retirés restent visibles à
part) ; « Envoyer à Claude » emporte les décisions. Demande de prix : UN dossier PDF par fournisseur (fabriqué dans le
carnet, sans bibliothèque) = page de garde + une page par produit avec SA photo, la grille 3 qualités × quantités et tout ce
qui manque (carton, poids, délai, matière, couleurs, garantie, certificats), pré-rempli quand on le sait ; l'Excel suit les
mêmes cases ; un produit du catalogue mis dans Comparer garde sa photo dans la demande ; la réponse expliquée. Questions :
le français sous chaque question sur l'écran tendu au vendeur, et la clé en français au-dessus du message. Module
`choix-1.9.0.html`, `construire-1.9.0.py` (part de la 1.8.0). Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.10.0 — 24/10/2026 : **L'étude rangée comme la page de Claude**. Dans l'onglet ⭐, une bascule en haut :
« ⭐ Choix de Claude » (la liste d'avant, inchangée) ou « 📊 Étude du … ». Une étude arrive par des fichiers de Claude
(clé `etude`, en plusieurs parties : un fichier par groupe), sans nouvelle version du carnet. Elle se range comme la page
« Achats Chine KYLO » : Groupe 1 à 5 (1er choix…), ✅ Ma liste, ⏳ Plus tard, 🔎 À relever, Tout ; en haut : achat en Chine,
à payer en plus (bateau, douane, transitaire), frais du voyage, ventes et gain attendus, place sur le bateau, jauge du budget,
feux ; chaque fiche : photo, nom chinois, feu, prix en Chine, arrivé au magasin, ton prix (+ ta marge), prix affiché par les
autres et deuxième prix, gain par pièce, contrôle, prix maximum à payer, quantité, ✅ Je prends / ⏳ Plus tard / ❌ Non,
détail du calcul, chinois à copier pour 1688, sources. « Mes chiffres » (budget, frais du voyage, marge, marchandage,
bateau, douane, budget tout compris) recalculent tout ; taille du texte Normal / Grand / Très grand. Les chiffres sont
ceux de la page, à l'unité près. Le gros de l'étude (textes, photos) est dans la réserve du téléphone (IndexedDB) ; le
carnet ne garde que la liste des études, les décisions et les réglages. Les produits d'une étude déjà arrivés dans ⭐ le
matin quittent la liste ⭐ en emportant leur décision. « Envoyer à Claude » emporte aussi les décisions des études.
Module `etude-1.10.0.html`, `construire-1.10.0.py` (part de la 1.9.0). Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

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
