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

Version 1.11.0 — 24/10/2026 : **Les cartes bien lues, les réponses en photos, l'agent, le cargo**.
A. Cartes de visite : 2e regard sur la photo (plus grande, plus contrastée, en négatif pour les bandeaux) ; TOUS les numéros
(2e portable, 2e fixe, « M.T. »), tous les e-mails (2e e-mail ; un portable écrit en e-mail n'efface plus le portable),
les 2 sites ; e-mails réparés (« _ » lu comme une espace, « © », domaine corrigé d'après le site ou le QR) et signalés ;
société « … LTD. / HOLDINGS », nom chinois complet à part (contrat), sinon la marque de son site (signalée) ; nom pinyin
(« Luo Jin Qi ») ; QR d'un catalogue → « 📖 Son catalogue en ligne » (plus pris pour un site ou un WeChat), QR doré lu par le
canal bleu. « Voir et corriger » : photo de la carte, cases lues (jaune) et douteuses (rouge, avec la raison), tout le texte lu
à copier, « Lecture de l'iPhone (Texte en direct) » qui remplace ce que le carnet avait lu. « 🔁 Relire mes cartes ».
B. « Fichier reçu sur WeChat » : le carnet dit à QUI il pense que c'est et pourquoi (numéro dans le fichier, nom dans le
nom du fichier, page de demande de prix), sinon il DEMANDE (ceux à qui on a demandé des prix en premier) avant de ranger.
C. « 📸 Sa réponse en photos » (sa fiche) : ses photos gardées ; sa photo au-dessus des cases (3 qualités × quantités) de
chaque produit de la demande ; message collé lu (« 3 = 28 ¥ — Xidi ») ; « Il ne l'a pas » ; c'est aussi « corriger sa liste ».
Chaque page de demande de prix porte un QR « KYLO F05 3 » : la page renvoyée en photo va toute seule au bon produit.
Une capture de tableau de prix (ITEM NO / QTY / RMB EXW / FOB / USD / MEAS / CBM) devient des prix sur ses modèles.
D. Étude : « 🏭 Qui le vend ? » sur chaque fiche (prix reçus des fournisseurs et de l'agent, comparés au prix maximum),
« Peut-être chez » (modèles de ses catalogues qui ressemblent), « ➕ Le demander à un fournisseur » (photo et nom chinois de
l'étude dans SA demande), « 📍 Où le chercher » (marchés de gros et usines en chinois, « Montrer au chauffeur », Plans).
Un fichier de Claude peut relier un modèle de catalogue à un produit de l'étude (`produits[].etude` / `offres[].etude`).
E. « ✅ Ma liste » → PDF pour l'agent (photo, n°, français + chinois, quantité, prix visé, MAXIMUM ; sans prix de vente)
et PDF complet pour moi ; l'agent a sa fiche, sa réponse se range comme celle d'un fournisseur.
F. « 🚢 Cargo et contrôle » (Fournisseurs et étude) : cargos de la recherche du 24/10, 10 questions (FR / 中文+EN), réponse
notée, comparaison en € par m³, « ⭐ Je choisis » → bateau, douane et transitaire de l'étude, entrepôt dans les contrats ;
contrôle (V-Trust, QIMA, cargo) ; vérifier la société avant l'acompte (licence, gsxt.gov.cn, message chinois).
Corrigée le 24/10 au soir (même numéro) : un prénom seul près du numéro (« Rosy ») devient le contact ; une marque qui contient « boss » n'est plus prise pour un poste.
Corrigée le 25/10 (même numéro, partie G — ce qu'ont appris les 6 vrais catalogues reçus sur WeChat) : familles Valise, Sac à dos,
Poubelle, Égouttoir, Salle de bain, Parapluie, Gourde, Parfum d'intérieur, Table d'appoint, Stylos et coffrets (avant « Téléphones »
pour un sac, « Alimentaire » pour une poubelle) ; une pièce détachée (« ABS-704 ») n'est plus un modèle ; cartes : « Contact » /
« Email » ne sont plus pris pour un nom, un bout de phrase de catalogue n'est plus une société (mais « Co. Ltd » et « Arts and
Crafts » restent des sociétés), e-mail et site corrigés seulement d'après un nom très proche ; la remarque du fournisseur (la
vérification de Claude) se lit en haut de SA fiche ; « Qui le vend ? » montre le modèle et sa photo quand un fournisseur a
plusieurs modèles reliés au même produit ; un fichier de Claude remplit aussi le nom chinois de la société, le 2e site, le
2e e-mail, le 2e numéro et le lien du catalogue.
Fichiers `suivi-1.11.0-*.js` + `suivi-1.11.0.css`, `construire-1.11.0.py` (part de la 1.10.0). Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.12.0 — 27/10/2026 : **Yiwu n'est pas Guangzhou, et chacun se retrouve dans WeChat**.
A. Villes : chaque fournisseur porte sa ville (`ville` : Yiwu ou Guangzhou). Les fiches d'avant sont de Guangzhou ; celles notées
à partir du 27/10 à 8 h (heure de Chine) sont de Yiwu (sauf celles venues d'un fichier de Claude, de l'Interprète ou de l'agent).
« 📍 Je suis à » en haut de 🏭 Fournisseurs : chaque nouveau fournisseur prend cette ville. À Yiwu le code commence par Y (Y01…),
à Guangzhou il reste F (F01…) ; chaque ville compte de son côté. Ceux notés à Yiwu avant la mise à jour (codes F) : « Leur donner
un code Y » (seulement si le code n'a pas servi : WeChat, demande de prix, contrat), ou les garder. La liste : deux groupes
(🛍️ Yiwu puis 🏙️ Guangzhou) et des puces de ville ; Sa fiche : la ville et « changer de ville ». Un fournisseur de Yiwu a le
marché de Yiwu et le lieu de rencontre « yiwu » (« 在义乌国际商贸城您的店铺见过 » dans la demande de prix et le mot WeChat ;
« Yiwu (sa boutique) » dans « Où l'avez-vous rencontré ? »). Les codes Y sont reconnus partout (QR « KYLO Y01 3 » des pages
de demande de prix, nom de fichier « KYLO-报价-Y01-… », « À qui ? »).
B. WeChat : le nom à donner dans WeChat est « CODE-Marque-Prénom » (« Y01-Bosstech-Rosy ») ; le mot à taper dans la recherche
est le code avec le tiret (« Y01- »), ou, s'il porte déjà un autre nom (« BAVIN-Lisa.1F084 NewAsia »), le premier mot de ce nom
(`wechat_nom`). Au stand : « 💬 Copier ce nom et ouvrir le scanner WeChat », puis « ✅ C'est fait ». Sa fiche : le mot à taper,
ou « Copier son numéro et ouvrir WeChat » / « Copier le nom » / « C'est fait » / « Il porte déjà un autre nom ». « À qui
envoyez-vous ? » montre le mot à taper. Nouvel écran « 💬 Mes fournisseurs dans WeChat » (entrée en haut de 🏭 Fournisseurs) :
tous, par ville, « ⏳ À nommer » / « ✅ Avec leur code », ceux à qui des prix ont été demandés d'abord, compteur ; le carnet
s'y rouvre au retour de WeChat, sur le dernier fournisseur touché.
C. Sa boutique à Yiwu (`yiwu` : district, porte, étage, rue, n° de boutique) : au stand et sur sa fiche, lue sur sa carte quand
elle y est (« 二区东7门3楼12街23456 », « Booth 23456, Street 12, F3, Gate 7, District 2 »), écrite en chinois en grand pour le
chauffeur ou le gardien. Questions au vendeur de Yiwu : mélanger les modèles (混批), un seul carton, livrer à l'entrepôt du
transitaire à Yiwu.
D. « 🛍️ Le marché de Yiwu » : qui vend quoi, par rayon et par district (recherche du 27/10), adresses en chinois pour le
chauffeur ; « 📍 Où le chercher » (l'étude) montre Yiwu en premier quand on y est.
« Envoyer à Claude » emporte `ville`, `code_avant`, `lieu_rencontre`, `wechat_nom`, `yiwu`.
Fichiers `suivi-1.12.0-*.js` + `suivi-1.12.0.css`, `construire-1.12.0.py` (part de la 1.11.0). Test rejouable :
`tests/test-carnet-1120.py`. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.13.0 — 28/10/2026 : **La commande dans le carnet, le vrai carton, la mémoire calme, WeChat sans « F59- »**.
A. « 📦 Commande » (onglet ⭐, 3ᵉ vue, et en haut de 🏭 Fournisseurs) : une commande arrive par un fichier de Claude (clé
`commande`, même bouton que les catalogues ; aucune version pour la suivante), rangée dans la réserve du téléphone. Totaux (à payer
en Chine, bateau + douane, pièces, gain) avec le calcul de l'étude et tes « Mes chiffres » ; par fournisseur, chaque produit (photo,
feu, prix, carton, arrivé, ton prix, prix affiché, gain, prix maximum, cartons − / +) ; « En plus » à cocher ; le bon de commande
chinois + anglais de chaque fournisseur (📋 Copier, 💬 Copier et ouvrir WeChat avec le mot à taper, 🛒 Mettre dans mes achats →
budget et « 📝 Contrat d'achat ») ; les blocs du fichier (manque, catalogue sans prix → « 💰 Lui demander ses prix », matériel,
à vérifier). Le carnet se rouvre sur la commande. « Envoyer à Claude » emporte `commandes_choix`.
B. « 🏭 Qui le vend ? » (étude) : le verdict se calcule avec le carton du fournisseur quand il est connu (dimensions, ou
`offres[].carton.m3` d'un fichier de Claude), et le dit.
C. Mémoire : un carnet gardé dans la réserve du téléphone n'affiche plus le bandeau ambre (un message calme par jour) ; la petite
mémoire garde une copie allégée (numéro 0 : la réserve passe devant) qui laisse la place aux petites choses (onglet, brouillon
« Au stand », filtres) et sert de secours ; si la réserve disparaît, alerte rouge et copie allégée ; Voyage : « 💾 Où ton carnet
est gardé » ; stockage persistant demandé.
D. WeChat : un fournisseur pas encore nommé dans WeChat n'a plus « F59- » comme mot à taper ; le carnet propose son prénom, sa
marque, son ID WeChat, et la case « Son nom dans mon WeChat » (recopié une fois) ; lui donner son code reste facultatif (replié).
Fichiers `suivi-1.13.0-*.js` + `suivi-1.13.0.css`, `construire-1.13.0.py` (part de la 1.12.0). Tests rejouables :
`tests/test-carnet-1130.py` (51 contrôles) et `tests/test-carnet-1130-reprise.py` (les 57 de la 1.12.0 ; E4, E6, E13 changés
exprès pour D). Rien de retiré.
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
