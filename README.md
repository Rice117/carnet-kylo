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

Version 1.14.0 — 28/10/2026 : **« 📤 Ma journée pour Claude »** (en haut de 🏭 Fournisseurs).
Ce qui a été noté aujourd'hui (ou depuis le dernier envoi, ou tout) part en deux fichiers faits dans le téléphone, sans Internet :
un PDF que Claude lit (page de consignes et sommaire ; une page par fournisseur : coordonnées, boutique de Yiwu, sa carte, la liste
de ses produits ; une page par produit noté avec SA photo, l'étiquette et le prix tapé ; les modèles de ses catalogues lus par le
carnet, 6 par page avec photo, référence, prix et carton, « à vérifier » ; ses réponses et panneaux en photo ; les pages WeChat
seulement si on coche), et `KYLO-journee-<jour>.json` (`format: kylo-pour-claude`, `quoi: journee`) avec les mêmes données en
chiffres, chaque produit renvoyant à sa partie et sa page du PDF. Ce qui vient d'un fichier de Claude ne repart pas. Les produits
notés sans fournisseur partent dans un groupe à part. Au-delà de 80 pages ou 22 Mo, le PDF est coupé en parties. « 📤 Partager »
envoie les fichiers ensemble (sinon 💾 un par un). L'étude en cours part en court (feu et prix maximum avec tes chiffres, ton
choix). Chaque ligne a sa clé (`o:…` / `p:…`) : Claude la renvoie dans `offres[].cle` et le prix relu se pose sur la bonne ligne.
Un prix posé par un fichier de Claude est marqué (`prix_claude_le`) et ne repart pas. Claude renvoie le fichier habituel (`kylo-import`).
Fichiers `suivi-1.14.0-a-journee.js` + `suivi-1.14.0.css`, `construire-1.14.0.py` (part de la 1.13.0). Tests rejouables :
`tests/test-carnet-1140.py` (31 contrôles), et les 51 + 57 contrôles de la 1.13.0 rejoués sur la 1.14.0. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.15.0 — 29/10/2026 : **Le carnet ne chauffe plus le téléphone ; « ✅ À contacter » en haut ; le bloc de codes-barres ne se perd plus**.
Mesuré d'abord (carnet de test aussi gros que le vrai : 132 fournisseurs, 3 760 modèles, 413 photos, 68 produits vus avec photo ;
processeur ralenti ×4) : chaque geste coûtait cher — toucher « ✅ À contacter » 5 fois : 18,7 s de calcul ; taper 20 lettres : 6,4 s ;
l'écran 🏭 Fournisseurs pesait 18 à 28 Mo parce que chaque photo y était recopiée en texte à chaque dessin. Désormais : 0,6 s ; 1,5 s ;
écran de 1,8 Mo ; au repos 0,5 %. Comment : les photos de l'écran principal passent par une adresse courte (`blob:`, gardée une fois)
et ne se chargent qu'en arrivant à l'écran (`loading="lazy"`) — les petits QR et les fenêtres ne changent pas (appui long →
« Enregistrer dans Photos ») ; les petites photos et les images du carnet sont lues en une seule fois dans la réserve ; un
enregistrement par geste (au plus tard 2,5 s après, et tout de suite en quittant l'application : `pagehide`, `visibilitychange`,
`freeze`) ; « ✅ À contacter » ne redessine que la fiche touchée ; les règles d'écriture des dates sont gardées ; l'appareil photo du
carnet s'éteint 12 s après (au lieu de 45 s). Rien ne change dans les données.
« ✅ À contacter » : une carte tout en haut de 🏭 Fournisseurs (WeChat, 📞, « ✔ Contacté » → « Déjà contactés », `contacte_le`) ;
le filtre « ✅ À contacter » marche aussi en vue « 📂 Par catégorie » (il était ignoré).
Codes-barres : la ligne du magasin est comprise même abîmée (point de l'iPhone, tiret long, espace insécable, minuscules, O pour 0,
milliers séparés, les deux colonnes copiées, plusieurs lignes d'un coup) ; plusieurs blocs (`C.blocs_suivants`, le suivant prend le
relais, `C.blocs_finis`) ; une copie à part (`localStorage kylo_blocs_v1`, numéro suivant qui ne recule jamais) remet les blocs si le
carnet est remplacé par un fichier ou effacé ; un fichier de Claude peut apporter `blocs` (📥) ; 📋 Coller ; l'astuce « Texte en
direct » de l'appareil photo. Ouvrir un fichier carnet demande confirmation dès qu'il y a des fournisseurs (avant : seulement des achats).
Fichiers `suivi-1.15.0.html`, `construire-1.15.0.py` (part de la 1.14.0). Test rejouable : `tests/test-carnet-1150.js` (85 contrôles,
compare chaque écran et les dates à la 1.14.0, et mesure les deux). Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.16.0 — 30/10/2026 : **Achats reliés au fournisseur ; le code-barres du carton ; un contrat sans numéro de carte, dans la ville du fournisseur**.
« 🛒 Ajouter un achat » commence par le fournisseur (recherche par code, nom, WeChat, produit ; les 30 plus récents en tête), puis montre
ses produits (vus au stand, demandés, puis les modèles de son catalogue qui intéressent ou ont un prix) avec photo et prix : on coche, on
tape pièces et prix obtenu, total en direct ; « ➕ Un autre produit de sa boutique » (photo, nom, description, prix, pièces) entre dans sa
fiche et dans la liste ; « Mettre N produits dans mes achats » relie chaque achat à son produit et à son fournisseur et lui donne son
code-barres de pièce (bloc du carnet) ; décocher un produit déjà acheté le sort des achats (deux appuis), il reste dans la fiche. L'achat
libre reste possible. L'onglet Achats est rangé par fournisseur (🛒 ajouter / enlever chez lui, 📝 son contrat, 🏷 codes-barres).
Code du carton : code de la pièce + « -C » + pièces dans ce carton, en Code 128 (encodeur dans le carnet, vérifié contre la table
standard et relu par le lecteur du carnet) ; dernier carton incomplet = son propre code ; « 📦 Tout dans un seul carton » ; un PDF
d'étiquettes pour le fournisseur (une par produit : ligne du contrat, photo, EAN-13 ; une par carton : KYLO EURGUINE, Conakry en
chinois, n° du contrat, 每箱 N 个, 箱号 k/T, Code 128 ; aucun prix) ; Arme 18 montre le vrai code. Contrat : section 3 « Comment vous
le payez » (Alipay, WeChat Pay, espèces, virement ; comptes DU VENDEUR avec le nom réel ; reçu signé et tamponné pour les espèces ;
les cases bancaires ne servent qu'au virement) ; alerte si le compte est celui de l'acheteur (KYLO, banque de France ou de Guinée) ou
ressemble à une carte Visa / Mastercard (pas UnionPay 62…), envoi en deux appuis, « 🗑 L'effacer » ; lieu de signature et entrepôt du
transitaire = la ville du fournisseur (义乌 / Yiwu), case « Ville où vous signez », adresse en français expliquée en chinois.
Changer la photo, le nom, la description : d'un achat (🗑 enlever, 📷 changer, description, 🔄 remplacer par un autre produit du même
fournisseur — le code-barres reste) et d'un produit noté (✏️ au stand et dans la fiche ; l'achat suit ; le même produit chez un autre
fournisseur ne change pas). Chiffres sous les codes-barres : jamais sous 14 px. Fichiers `suivi-1.16.0.html`, `suivi-1.16.0-contrat.html`,
`suivi-1.16.0-achats.html`, `construire-1.16.0.py` (part de la 1.15.0). Tests : `tests/test-carnet-1160.js` (94 contrôles, gros carnet),
`test-maj-1160.js`, `test-reserve-1160.js`. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.
Relecture indépendante avant mise en ligne : achats faits avant chez le même fournisseur reliés (même nom) ou montrés à part ; double
appui sans doublon ; les messages « appuyez encore » passent par-dessus les fenêtres ouvertes (`avertir` range son message dans la
fenêtre ouverte, `fermerBoite` le rend à la page) ; remplacer par un produit déjà acheté refusé ; retrait = frais remis au prorata ;
carte chinoise du vendeur pas confondue avec celle de l'acheteur ; IBAN FR/GN reconnus ; « Consignes pour le fournisseur » : un code
par carton. `tests/test-carnet-1160.js` : 112 contrôles.

Version 1.17.0 — 30/10/2026 : **L'argent, les cartons et les contrats ne se perdent plus**. 🧭 « À faire maintenant » en haut de
Fournisseurs et d'Achats : la prochaine chose à faire, fournisseur par fournisseur, calculée sur le carnet (contrat à envoyer, à faire
signer, acompte, livraison proche, retard avec la relance chinoise prête, contrôle, solde, paiement sans reçu, codes-barres, pièces par
carton, demandes de prix sans réponse, bloc de codes qui s'épuise, budget, copie de sécurité), le plus urgent en rouge, chaque ligne avec
son bouton ; lu sans créer de contrat. 💵 Paiements de chaque contrat (acompte, solde, « autre » montré mais pas compté ; mode, date,
photo du reçu ; montant en ¥ figé au paiement ; devise sans taux refusée ; trop-payé en deux appuis ; étapes « acompte / solde payé »
cochées toutes seules et seules celles-là décochées au retrait ; étapes cochées à la main avant la 1.17.0 crues, avec « notez le montant »).
⏰ Pénalité de l'article 4 (par jour, plafonnée, annulation possible) comptée seulement pour un contrat signé, retirée du « reste » partout.
📦 Réception chez le cargo : scanner des codes de carton à la chaîne (résultat affiché après la fermeture de l'écran de scan ; même
étiquette relue à la réouverture pas comptée deux fois ; caméra fermée après 3 minutes sans lecture ; verrou toujours rendu), carton en
trop signalé, code de pièce reconnu, contrôle de chaque produit (pièces, comme l'échantillon, problèmes, photo), date de réception
seulement au 1er carton ou au verdict ; ✅ conforme → solde (pénalité retirée) ; ❌ → réclamation de l'article 7 en chinois + anglais,
avec sa traduction. Seules les lignes du contrat (prix et quantité) sont attendues, contrôlées, facturées. 🧾 Liste de colisage (sans prix,
toutes les lignes du contrat) et facture commerciale (prix du contrat, case signature et cachet du vendeur) en un PDF de 2 pages.
🔎 Code de crédit social du vendeur vérifié sans Internet (GB 32100-2015, et le 2e chiffre de contrôle du code d'organisation, GB 11714),
type (société / commerçant individuel) et ville d'enregistrement ; « O » tapé pour 0 corrigé et gardé. ✈️ Livraison après la fin du
voyage : qui contrôlera. Bilan de chaque fournisseur sur sa fiche. Argent : « Ce que je dois encore aux fournisseurs ».
Fichiers `suivi-1.17.0.html`, `suivi-1.17.0-reception.html`, `suivi-1.17.0-pilote.html`, `construire-1.17.0.py` (part de la 1.16.0).
Tests : `tests/test-carnet-1170.js` (99 contrôles), la suite 1.16.0 rejouée (112), `test-maj-1170.js` (7), `test-reserve-1170.js` (10).
Relecture indépendante avant mise en ligne, toutes ses remarques corrigées et rejouées dans le test. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.18.0 — 30/10/2026 : **Le contrôle complet de A à Z**. Cinq contrôles « comme l'utilisateur » (le voyage depuis un carnet
vide ; argent et planification ; fournisseurs et stand ; comparer, négocier, acheter, envoyer ; contrat → réception), chaque écran et
chaque bouton, les calculs refaits à la main, la cohérence entre écrans : 150 défauts (20 graves). Corrigés en six chantiers + un
morceau commun + un morceau d'assemblage, chacun avec un test qui échoue sur la 1.17.0 et passe sur la 1.18.0. Règles désormais :
**un seul coût de revient** partout (frais = le plus grand entre l'estimation du voyage et les frais notés ; pénalité de retard
retirée) ; **marge = (vente − coût) ÷ vente** partout (anciennes marges converties sans changer les prix) ; **le prix de vente se
décide** (plus de marge mise d'office ; un produit sans prix est « à fixer », pas « prêt ») ; **chaque prix garde sa devise**
(devise du marché proposée : ¥ en Chine ; contrat et facture en yuans justes, nombres avec un point en chinois) ; **rien ne se
perd** (deux appuis, « Fermer » demande, fournisseur avec achats jamais supprimé, import de Claude qui ne mélange plus deux
fournisseurs, « Voir un exemple » qui n'efface plus rien, cartes de visite dans le fichier « Enregistrer », « 📸 Copie complète »
avec toutes les photos) ; **jamais retaper** (prix négocié → achat, pièces par carton au stand → achat → cartons → conteneur,
date du contrat → conteneur, un seul budget, une seule liste de frais, un seul registre d'acomptes) ; contrat signé puis modifié :
alerte et avenant ; le bloc ne redonne jamais un code déjà porté ; livraison incomplète acceptée ; envoi au magasin avec la quantité
reçue ; « Préparer mon voyage » avec date de retour ; nombres « 1 400 » / « 100 pièces » lus justes ; rien sous 14 px, contrastes.
Fichiers `suivi-1.18.0-commun.html`, `suivi-1.18.0-F1…F6-*.html`, `suivi-1.18.0-Z-assemblage.html`, `construire-1.18.0.py`
(part de la 1.17.0). Tests : `test-commun-1180.js`, `test-F1…F6-*-1180.js`, `test-assemblage-1180.js`, plus les suites 1.17.0 et
1.16.0 rejouées, `test-maj-1180.js`, `test-reserve-1180.js`. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.19.0 — 30/10/2026 : **Les caisses de l'argent**. Chaque frais va dans une caisse, et chaque caisse se partage entre
les produits avec sa propre clé : 🛍 marchandise (le prix de chaque produit) ; 🤝 achat sur place (accompagnateur, interprète,
commission de l'agent, échantillons, téléphone, banque) selon la valeur ; ✈️ voyage (billet, hôtel, repas, taxi, visa) selon la
valeur ; 🚢 transport (transitaire en Chine, bateau au volume des cartons, avion au poids) ; 🛃 douane = % de (achat + transport),
transitaire et port à l'arrivée selon la valeur ; 🏠 hors coût (« Ne pas répartir » : achats personnels, cadeaux) dans l'argent
sorti, jamais dans le coût des produits. Une caisse compte l'estimation tant que les frais notés ne la dépassent pas, ou jusqu'à
« ✅ Tout est noté » ; le surplus d'estimation se partage selon l'estimation de chaque produit. C'est la formule de l'étude
« Achats Chine KYLO » : arrivé = (achat + bateau) × (1 + douane) + achat × (transitaire + voyage). Réglages dans l'onglet Frais
(🧺 → ⚙ Régler mes caisses), proposés depuis l'étude quand il y en a une ; rien ne compte avant « ✅ Garder » : jusque-là, le
calcul de la 1.18.0 est inchangé. Le % du voyage est celui qui est tapé (jamais « tous les frais ÷ budget »). « Voyage à part » :
aucun produit ne le porte, il reste dans l'argent investi.
Nouveau : la fenêtre d'un frais propose sa caisse ; 7 types de frais ; « 🧮 Son coût » (le coût d'un produit, caisse par caisse)
dans Achats ; « L'argent à prévoir, caisse par caisse » (compté, quand payer, payé, reste) et « À la fin » dans Argent ; 🧭 demande
les réglages qui manquent et signale les cartons pas mesurés (ou sans poids, en avion). Un prix vu dans Comparer est estimé de la
même façon. Corrigé : le fichier envoyé au magasin portait la version « 1.18.0 » écrite en dur ; il donne, pour
chaque produit, frais notés + estimés = sa part des caisses. Relu par un second contrôle indépendant (9 défauts corrigés).
Fichiers `suivi-1.19.0-caisses.html`, `construire-1.19.0.py` (part de la 1.18.0). Tests : `test-caisses-1190.js` (38 contrôles,
chaque coût refait à la main), plus les suites 1.18.0, 1.17.0 et 1.16.0 rejouées, `test-maj-1190.js`, réserve. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.20.0 — 31/10/2026 : **★ Ma liste, et une seule règle pour les listes**. Dans l'onglet ⭐, à côté de la liste de Claude,
« ★ Ma liste » réunit les modèles étoilés (★ M'intéresse) de tous les catalogues : prix du fournisseur, coût rendu au magasin, prix
affiché à Conakry (tapé, sinon celui de la liste de Claude pour ce modèle, sinon le marché connu), 2ᵉ prix, marge sur la vente et sur
le coût, feu, « à ne pas dépasser », quantité, total, « ☆ Retirer », « 📋 Copier ma liste ». Les deux listes comptent le même coût (R1 : l'achat, sinon
Comparer, sinon l'estimation — avec les caisses, ou sans caisses exactement celle d'avant) et une seule règle « au moins +N % sur
mon coût », la même que l'étude (75 par défaut), au lieu de 35 % de la vente ; « à ne pas dépasser » arrondi vers le bas. Relu par un
second contrôle indépendant (8 défauts corrigés). Sur chaque fiche, « 🧮 Comment ce % est
calculé » montre le prix qui compte (achat, prix reçu, stand ou fourchette), le bateau, la douane, le reste, le coût rendu, le 2ᵉ prix
et les deux pourcentages. Fichiers `suivi-1.20.0-listes.html`, `construire-1.20.0.py` (part de la 1.19.0). Tests :
`test-listes-1200.js` (35 contrôles), plus les suites 1.19.0, 1.18.0, 1.17.0 et 1.16.0 rejouées, `test-maj-1200.js`, réserve. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.21.0 — 31/10/2026 : **Le prix dit au stand, dans ★ Ma liste**. Sur chaque fiche de « ★ Ma liste » (sauf un modèle déjà
acheté), une case « 💬 Prix dit par le fournisseur » en ¥ : pendant la frappe (ou la dictée 🎤, quand le téléphone la permet : « trente-
cinq », « douze virgule cinq »), les dollars, le coût rendu au magasin en Guinée et le verdict (🟢 / 🟡 / 🔴 avec le maximum en ¥,
arrondi vers le bas), sans redessiner l'écran ; le feu de la fiche suit. En quittant la case (ou « ✓ Garder » après la dictée),
le prix est gardé une seule fois : dans l'offre de Comparer ET le modèle du catalogue s'il y a une offre (anciens prix dans leur
historique, avec leur devise ; la date de visite ne bouge pas), sinon comme prix du modèle (en ¥, daté, « prix dit au stand ») ; une
offre à plusieurs qualités n'est jamais écrasée ; le même prix redit ne change rien ; la fiche se met à jour sans redessiner les cases.
Relu par un second contrôle indépendant (9 défauts corrigés). Le même calcul que ★ Ma liste (1.20.0). Fichiers `suivi-1.21.0-prix-au-stand.html`,
`construire-1.21.0.py` (part de la 1.20.0). Tests : `test-prix-stand-1210.js` (27 contrôles), plus les suites 1.20.0, 1.19.0, 1.18.0, 1.17.0 et
1.16.0 rejouées, `test-maj-1210.js`, réserve. Rien de retiré.
⚠ Même remarque pour `KYLO-Achats.html`.

Version 1.22.0 — 01/11/2026 : **Ta commande par fichier de Claude**. Un fichier de Claude (📥, format kylo-import) peut porter, pour
un fournisseur, des `achats` ({ ref, quantite, prix_unitaire, devise, famille, note, cle }) : l'aperçu les montre ligne par ligne
(montant, mis à jour ou nouveau, retirés, gardés, en double, introuvables, contrat déjà envoyé ou signé), puis « ✅ Ajouter au carnet »
les met dans « Mes achats » par le même chemin que « 🛒 Acheter chez » (code-barres du bloc, famille du magasin donnée par le fichier,
carton, photo du modèle, marge à fixer, contrat qui suit, messages gardés). Jamais en double : un achat déjà relié est mis à jour, un
achat noté à la main avec la même référence est relié ; une ligne déjà posée et changée ou supprimée à la main depuis n'est plus
touchée ; « quantite » 0 retire seulement un achat posé par un fichier. Un fichier peut aussi `reunir` une fiche qu'un fichier de
Claude avait créée en trop (même fournisseur) : modèles, étoiles, prix (un prix dit au stand reste le prix), lignes de Comparer et achats
passent, sans doublon. Relu par un second contrôle indépendant (10 points, dont un nom de fonction déjà pris dans le carnet et un achat
doublé à la réunion : tous corrigés). Fichiers `suivi-1.22.0-commande-par-fichier.html`, `construire-1.22.0.py` (part de la 1.21.0).
Tests : `test-achats-1220.js` (31 contrôles), plus les suites 1.21.0, 1.20.0, 1.19.0, 1.18.0, 1.17.0 et 1.16.0 rejouées,
`test-maj-1220.js`, réserve. Rien de retiré.
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
