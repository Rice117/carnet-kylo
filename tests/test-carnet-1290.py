#!/usr/bin/env python3
"""Carnet 1.29.0 — les fichiers de Claude arrivent par Azuska Z ; le carnet entier part à Azuska Z.
Contrôle rejouable dans un vrai Chromium, taille téléphone, avec un faux Azuska Z (mêmes portes, même code d'envoi).
Usage : python3 -I tests/test-carnet-1290.py <dossier 1.28.0> <dossier 1.29.0> <dossier captures>
Ce qu'il prouve :
  N1 un téléphone en 1.28.0 passe en 1.29.0 sans rien perdre ; aucune erreur JavaScript ;
  N2 sans code d'envoi : aucun bandeau, AUCUNE demande à Azuska Z ;
  N3 avec le code : à l'ouverture, un bandeau vert dit combien de fichiers Claude a déposés et leur poids ; rien n'est
     téléchargé tant que Riche n'a pas touché « Ajouter au carnet » ; le code part dans l'en-tête X-Code-Envoi ;
  N4 « 📥 Ajouter au carnet » : les fichiers passent un par un par le même chemin qu'à la main (modèles, prix, frais 1.28.0),
     le bilan dit « 2 fichiers ajoutés sur 2 » ; rouvert : plus de bandeau ; un 3e fichier déposé → « 1 fichier » ;
  N5 un code faux : pas de bandeau, et le bouton dit « Code d'envoi incorrect » ; Azuska Z éteint : rien ne casse ;
  N6 la carte « 3. Directement vers Azuska Z » (onglet « Envoyer au magasin ») : adresse internet pré-remplie, deux boutons,
     rien sous 14 px ;
  N7 « 📤 Envoyer tout le carnet » : la copie du jour part en morceaux de 4 Mo (gros carnet = plusieurs morceaux), Azuska Z
     reçoit EXACTEMENT le carnet (voyage, achats, fournisseurs), rien n'est partagé ni téléchargé sur le téléphone ;
     « Enregistrer » marche toujours comme avant (fichier) ;
  N8 un morceau qui échoue (erreur 500) est renvoyé ; un code refusé (401) arrête tout avec un message clair ;
  N9 réseau coupé pendant « Envoyer tout » : « Pas envoyé » en français, la dernière sauvegarde N'EST PAS changée (le rappel 💾
     reste), pas d'avis « Copie du jour » ; envoi réussi : le carnet compte comme sauvegardé ;
  N10 porte fermée (429, trop de codes faux) : le carnet dit « Azuska Z a répondu : « … attends dix minutes. » », jamais
     « n'a pas répondu », jamais « .. », et ne conseille pas d'attendre internet ; aucun avis « 💾 » collé sous l'avis
     déjà affiché pendant « Envoyer tout » ;
  N0 garde réseau : seul 127.0.0.1 est joignable ; l'adresse internet d'Azuska Z est servie sur place (jamais le vrai
     azuska.kyloeurguine.com) ; une sonde vers une adresse qui n'existe pas prouve que la garde est bien branchée ; chaque
     demande vue par Chromium hors de l'atelier est passée par la garde.
  (La version en ligne, en https, est contrôlée par tests/test-carnet-1290-https.py.)
"""
import base64, json, os, re, sys, threading, time, uuid
import http.server, socketserver
from urllib.parse import urlparse, parse_qs
from playwright.sync_api import sync_playwright

D1280, D1290, CAPT = sys.argv[1:4]
os.makedirs(CAPT, exist_ok=True)
PORT, PORT_AZ = 8781, 8782
ETAT = {'racine': D1280}

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ETAT['racine'], **k)
    def end_headers(self): self.send_header('Cache-Control', 'no-store'); super().end_headers()
    def log_message(self, *a): pass

# ---------------------------------------------------------------- le faux Azuska Z
PIXEL = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=='
def kylo(titre, nom, produits, frais=None):
    d = {'format': 'kylo-import', 'v': 1, 'titre': titre, 'fournisseurs': [{'nom': nom, 'societe': nom, 'produits': produits}]}
    if frais: d['frais'] = frais
    return json.dumps(d).encode()
AZ = {'code': 'ABCDEF', 'fichiers': {}, 'demandes': [], 'morceaux': {}, 'recus': [], 'panne': 0, 'refus401': False, 'eteint': False, 'porte': False}
PORTE = "Trop de codes faux : attends dix minutes."      # le message exact d'Azuska Z 2.56.0 (porte fermée 10 minutes)
def deposer(nom, titre, octets):
    i = uuid.uuid4().hex[:20]
    AZ['fichiers'][i] = {'id': i, 'nom': nom, 'titre': titre, 'octets': octets}
deposer('CARNET-DE-VOYAGE-IMPORT-TEST-A.json', 'Base de prix (essai A)',
        kylo('Essai A', 'Usine Essai A', [{'ref': 'TA-%03d' % k, 'prix': 10 + k, 'devise': 'CNY', 'photo': PIXEL} for k in range(40)]))
deposer('CARNET-DE-VOYAGE-IMPORT-TEST-B.json', 'Complément (essai B)',
        kylo('Essai B', 'Usine Essai B', [{'ref': 'TB-1', 'prix': 7, 'devise': 'CNY'}, {'ref': 'TB-2', 'prix': 9.6, 'devise': 'CNY'}]))

class A(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Code-Envoi')
        self.send_header('Access-Control-Expose-Headers', 'Content-Length')
    def repondre(self, code, obj=None, octets=None, ctype='application/json'):
        corps = octets if octets is not None else json.dumps(obj).encode()
        self.send_response(code); self.cors(); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(corps))); self.end_headers(); self.wfile.write(corps)
    def do_OPTIONS(self):
        self.send_response(204); self.cors(); self.end_headers()
    def code_ok(self):
        c = re.sub(r'[^A-Z0-9]', '', (self.headers.get('X-Code-Envoi') or '').upper())
        return c == AZ['code'] and not AZ['refus401']
    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        AZ['demandes'].append(('GET', u.path, self.headers.get('X-Code-Envoi'), q.get('id', [''])[0]))
        if u.path != '/api/carnet/fichiers-de-claude': return self.repondre(404, {'ok': False})
        if AZ['porte']: return self.repondre(429, {'ok': False, 'erreur': PORTE})
        if not self.code_ok(): return self.repondre(401, {'ok': False, 'erreur': "Code d'envoi incorrect. Il est affiché dans Azuska Z → Fiches produits."})
        if 'id' in q:
            f = AZ['fichiers'].get(q['id'][0])
            if not f: return self.repondre(404, {'ok': False, 'erreur': 'absent'})
            return self.repondre(200, octets=f['octets'])
        return self.repondre(200, {'ok': True, 'fichiers': [{'id': f['id'], 'nom': f['nom'], 'titre': f['titre'], 'taille': len(f['octets']), 'modifie': '2026-11-09T12:00:00Z'} for f in AZ['fichiers'].values()]})
    def do_POST(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        n = int(self.headers.get('Content-Length') or 0); corps = self.rfile.read(n) if n else b''
        AZ['demandes'].append(('POST', u.path, self.headers.get('X-Code-Envoi'), u.query))
        if u.path != '/api/carnet/sauvegarde': return self.repondre(404, {'ok': False})
        if AZ['porte']: return self.repondre(429, {'ok': False, 'erreur': PORTE})
        if not self.code_ok(): return self.repondre(401, {'ok': False, 'erreur': "Code d'envoi incorrect."})
        depot = q.get('depot', [''])[0]
        if q.get('finir') == ['1']:
            m = int(q['morceaux'][0]); parts = AZ['morceaux'].get(depot, {})
            if any(i not in parts for i in range(m)): return self.repondre(400, {'ok': False, 'erreur': 'morceau manquant'})
            tout = b''.join(parts[i] for i in range(m))
            c = json.loads(tout.decode('utf-8'))
            AZ['recus'].append({'morceaux': m, 'taille': len(tout), 'carnet': c})
            return self.repondre(200, {'ok': True, 'achats': len(c.get('achats', [])), 'fournisseurs': len(c.get('fournisseurs', [])),
                                       'message': 'Carnet reçu par Azuska Z : %d achat(s), %d fournisseur(s).' % (len(c.get('achats', [])), len(c.get('fournisseurs', [])))})
        i = int(q['n'][0])
        if AZ['panne'] > 0 and i == 1: AZ['panne'] -= 1; return self.repondre(500, {'ok': False, 'erreur': 'panne'})
        AZ['morceaux'].setdefault(depot, {})[i] = corps
        return self.repondre(200, {'ok': True, 'recu': len(corps)})

socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.ThreadingTCPServer(('127.0.0.1', PORT), H); threading.Thread(target=srv.serve_forever, daemon=True).start()
saz = socketserver.ThreadingTCPServer(('127.0.0.1', PORT_AZ), A); threading.Thread(target=saz.serve_forever, daemon=True).start()
URL = 'http://127.0.0.1:%d/index.html' % PORT
ADR_AZ = 'http://127.0.0.1:%d' % PORT_AZ

total = [0, 0]; echecs = []
def verif(nom, ok, info=''):
    total[0] += 1
    if ok: total[1] += 1; print('  ✔', nom)
    else: echecs.append(nom); print('  ✘', nom, '—', str(info)[:300])

BASE = """(() => { const j = (n) => new Date(Date.now() - n*86400000).toISOString();
  C.fournisseurs = [
    { id:'f1', code:'F84', nom:'Louie Liu — Lonwe', contact:'Louie Liu', ville:'Guangzhou', decision:'contacter', le:j(15).slice(0,10), vu_le:j(15), source:'carte', docs:[], produits:[{id:'p1',ref:'GS-1',prix:12,devise:'USD',note:'à moi', interesse:true}], mobile:'15869535039' } ];
  C.achats = [{ id:'a1', nom:'Frontale rechargeable', quantite: 240, prix: 7, devise:'CNY', fournisseur_id:'f1' }];
  C.voyage = Object.assign(C.voyage || {}, { nom: 'Chine octobre 2026' }); sauverLocal(); })()"""
OUVERT = "window.kyloReserveLue === true"
# Garde réseau (contrôle du 09/11) : rien ne doit sortir de l'atelier, surtout pas vers le vrai Azuska Z.
SORTIES, SUR_PLACE, TOUTES = [], [], []
LOCAL = re.compile(r'^(https?://127\.0\.0\.1:|data:|blob:|chrome-extension:)')
def garde_reseau(route):
    u = route.request.url
    if LOCAL.match(u): return route.continue_()
    if u.startswith('https://azuska.kyloeurguine.com'):   # le carnet appelle seul son adresse par défaut (course du N6) :
        SUR_PLACE.append(u)                                # réponse sur place, comme un ordinateur éteint — rien ne sort
        return route.fulfill(status=503, body='{"ok":false,"erreur":"atelier"}', headers={'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'})
    SORTIES.append(u); return route.abort()
def az(pg): return [d for d in AZ['demandes']]

with sync_playwright() as p:
    nav = p.chromium.launch()
    ctx = nav.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=1, is_mobile=True, has_touch=True, accept_downloads=True)
    ctx.route('**/*', garde_reseau)
    ctx.on('request', lambda r: TOUTES.append(r.url))
    pg = ctx.new_page(); erreurs = []
    pg.on('pageerror', lambda e: erreurs.append(str(e)))
    print('N1 — 1.28.0 → 1.29.0')
    pg.goto(URL); pg.wait_for_function(OUVERT, timeout=60000)
    pg.evaluate(BASE)
    avant = pg.evaluate("JSON.stringify({f: C.fournisseurs.length, a: C.achats.length, n: C.voyage.nom})")
    ETAT['racine'] = D1290
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000)
    verif('N1 version 1.29.0', pg.evaluate("window.KYLO_APPLICATION") == '1.29.0' and pg.evaluate("window.KYLO_BOITE_CLAUDE") == '1.29.0')
    verif('N1 rien perdu au passage', pg.evaluate("JSON.stringify({f: C.fournisseurs.length, a: C.achats.length, n: C.voyage.nom})") == avant, avant)

    print('N2 — sans code')
    pg.wait_for_timeout(4500)
    verif('N2 pas de bandeau sans code', pg.query_selector('#c29_bandeau') is None)
    verif('N2 aucune demande à Azuska Z sans code', len(AZ['demandes']) == 0, AZ['demandes'])

    print('N3 — avec le code')
    pg.evaluate("localStorage.setItem('kylo_adresse_azuska', '%s'); localStorage.setItem('kylo_code_azuska', 'ABC-DEF')" % ADR_AZ)
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000)
    pg.wait_for_selector('#c29_bandeau', timeout=15000)
    txt = pg.inner_text('#c29_bandeau')
    verif('N3 le bandeau dit « 2 fichiers » et leur poids', '2 fichiers' in txt and re.search(r'\(\d+ Ko\)|\(\d+,\d Mo\)', txt) and 'Base de prix (essai A)' in txt, txt)
    gets = [d for d in AZ['demandes'] if d[0] == 'GET']
    verif('N3 seulement la liste a été demandée (rien téléchargé sans geste)', all(d[3] == '' for d in gets) and len(gets) >= 1, gets)
    verif('N3 le code part dans X-Code-Envoi', all(d[2] == 'ABC-DEF' for d in gets), gets)
    pg.screenshot(path=os.path.join(CAPT, 'c29-bandeau.png'))
    taille_police = pg.evaluate("parseFloat(getComputedStyle(document.querySelector('#c29_bandeau')).fontSize)")
    verif('N3 bandeau lisible (≥ 16 px)', taille_police >= 16, taille_police)

    print('N4 — Ajouter au carnet')
    pg.click('#c29_bandeau button.vert')
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /fichiers? de Claude ajouté.* sur 2/.test(h.innerText); }", timeout=120000)
    bilan = pg.inner_text('#contenuBoite')
    verif('N4 bilan « 2 fichiers de Claude ajoutés sur 2 »', '2 fichiers de Claude ajoutés sur 2' in bilan, bilan)
    pg.screenshot(path=os.path.join(CAPT, 'c29-bilan.png'))
    res = pg.evaluate("""() => { const F = mkFournisseurs(); const a = F.find(f => /Essai A/.test(f.nom || f.societe || '')), b = F.find(f => /Essai B/.test(f.nom || f.societe || ''));
      return { a: a ? ctProduits(a).length : -1, aprix: a ? ctProduits(a).filter(p => p.prix > 0).length : -1, b: b ? ctProduits(b).map(p => p.ref + ':' + p.prix).sort().join(',') : '', recus: Object.keys(C.c29_recus || {}).length,
        louie: (F.find(f => f.id === 'f1') || {}).produits.length }; }""")
    verif('N4 les 40 modèles de A, avec leur prix', res['a'] == 40 and res['aprix'] == 40, res)
    verif('N4 les 2 modèles de B (9,6 ¥ compris)', res['b'] == 'TB-1:7,TB-2:9.6', res)
    verif('N4 les 2 fichiers notés comme reçus', res['recus'] == 2, res)
    verif('N4 ce que Riche avait noté est intact', res['louie'] == 1, res)
    ids_telecharges = [d[3] for d in AZ['demandes'] if d[0] == 'GET' and d[3]]
    verif('N4 chaque fichier téléchargé une seule fois', len(ids_telecharges) == 2 and len(set(ids_telecharges)) == 2, ids_telecharges)
    pg.evaluate("fermerBoite()")
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000); pg.wait_for_timeout(5000)
    verif('N4 rouvert : plus de bandeau (rien de nouveau)', pg.query_selector('#c29_bandeau') is None)
    deposer('CARNET-DE-VOYAGE-IMPORT-TEST-C.json', 'Complément (essai C)', kylo('Essai C', 'Usine Essai C', [{'ref': 'TC-1', 'prix': 3, 'devise': 'CNY'}]))
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000)
    pg.wait_for_selector('#c29_bandeau', timeout=15000)
    verif('N4 un 3e fichier déposé : « 1 fichier »', '1 fichier pour ton carnet' in pg.inner_text('#c29_bandeau'), pg.inner_text('#c29_bandeau'))
    pg.click('#c29_bandeau button.gris')
    verif('N4 « Plus tard » ferme le bandeau', pg.query_selector('#c29_bandeau') is None)

    print('N5 — code faux, Azuska Z éteint')
    pg.evaluate("localStorage.setItem('kylo_code_azuska', 'ZZZ-ZZZ')")
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000); pg.wait_for_timeout(5000)
    verif('N5 code faux : pas de bandeau', pg.query_selector('#c29_bandeau') is None)
    pg.evaluate("c29Recevoir()"); pg.wait_for_timeout(1500)
    toast = pg.evaluate("document.body.innerText")
    verif('N5 le bouton dit « Code d\'envoi incorrect »', "Code d'envoi incorrect" in toast, toast[-400:])
    verif('N5 les mots justes : « Azuska Z a répondu », pas « n\'a pas répondu », pas de « .. »',
          "Azuska Z a répondu : « Code d'envoi incorrect" in toast and "pas répondu" not in toast and '..' not in toast, toast[-400:])
    pg.evaluate("localStorage.setItem('kylo_adresse_azuska', 'http://127.0.0.1:9'); localStorage.setItem('kylo_code_azuska', 'ABC-DEF')")
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000); pg.wait_for_timeout(5000)
    verif('N5 Azuska Z éteint : pas de bandeau, pas d\'erreur', pg.query_selector('#c29_bandeau') is None and not erreurs, erreurs)
    pg.evaluate("localStorage.setItem('kylo_adresse_azuska', '%s')" % ADR_AZ)

    print('N6 — la carte « Directement vers Azuska Z »')
    pg.evaluate("localStorage.removeItem('kylo_adresse_azuska')")
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000)
    pg.evaluate("allerA('envoi')"); pg.wait_for_selector('#c29_carte', timeout=10000)
    verif('N6 adresse internet pré-remplie', pg.input_value('#adresseAzuska') == 'https://azuska.kyloeurguine.com', pg.input_value('#adresseAzuska'))
    boutons = pg.evaluate("[...document.querySelectorAll('#c29_carte button')].map(b => b.innerText)")
    verif('N6 deux boutons (Recevoir / Envoyer tout)', len(boutons) == 2 and 'Recevoir' in boutons[0] and 'Envoyer tout' in boutons[1], boutons)
    petit = pg.evaluate("[...document.querySelectorAll('#c29_carte, #c29_carte *')].map(e => parseFloat(getComputedStyle(e).fontSize)).filter(t => t < 14)")
    verif('N6 rien sous 14 px dans la carte', not petit, petit)
    pg.locator('#c29_carte').scroll_into_view_if_needed(); pg.screenshot(path=os.path.join(CAPT, 'c29-carte.png'))
    pg.fill('#adresseAzuska', ADR_AZ); pg.dispatch_event('#adresseAzuska', 'change')
    verif('N6 l\'adresse tapée est gardée pour les boutons', pg.evaluate("localStorage.getItem('kylo_adresse_azuska')") == ADR_AZ)

    print('N7 — Envoyer tout le carnet')
    # un carnet de plus de 4 Mo : 6 000 modèles notés (sans photo) chez un fournisseur
    pg.evaluate("""() => { const f = { id:'fgros', code:'Y99', nom:'Gros catalogue', ville:'Yiwu', docs:[], produits: [] };
      for (let i = 0; i < 6000; i++) f.produits.push({ id:'g'+i, ref:'GROS-'+i, prix: (i % 50) + 1, devise:'CNY', categorie:'Catégorie assez longue pour faire du poids ' + i, note: 'x'.repeat(600) });
      C.fournisseurs.push(f); sauverLocal(); }""")
    telechargements = []
    pg.on('download', lambda d: telechargements.append(d.suggested_filename))
    pg.evaluate("window.__partage = 0; navigator.share = async () => { window.__partage++; }; navigator.canShare = () => true;")
    AZ['panne'] = 1
    pg.evaluate("c29EnvoyerTout()")
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /Carnet reçu par Azuska Z|Pas envoyé/.test(h.innerText); }", timeout=180000)
    fin = pg.inner_text('#contenuBoite')
    verif('N7 « ✅ Carnet reçu par Azuska Z »', 'Carnet reçu par Azuska Z' in fin, fin)
    r = AZ['recus'][-1] if AZ['recus'] else {}
    c = r.get('carnet') or {}
    verif('N7 envoyé en plusieurs morceaux de 4 Mo (gros carnet)', r.get('morceaux', 0) >= 2 and r.get('taille', 0) > 4 * 1024 * 1024, {k: r.get(k) for k in ('morceaux', 'taille')})
    verif('N7 Azuska Z a EXACTEMENT le carnet (voyage, achats, fournisseurs)', c.get('voyage', {}).get('nom') == 'Chine octobre 2026' and len(c.get('achats', [])) == 1
          and any(f.get('id') == 'fgros' and len(f.get('produits', [])) == 6000 for f in c.get('fournisseurs', [])), {'voyage': c.get('voyage', {}).get('nom'), 'achats': len(c.get('achats', []))})
    verif('N7 rien partagé ni téléchargé sur le téléphone', pg.evaluate("window.__partage") == 0 and not telechargements, (pg.evaluate("window.__partage"), telechargements))
    verif('N8 le morceau en panne (500) a été renvoyé', AZ['panne'] == 0 and r.get('morceaux', 0) >= 2)
    pg.screenshot(path=os.path.join(CAPT, 'c29-envoye.png'))
    pg.evaluate("fermerBoite()")
    pg.evaluate("enregistrerCarnet()"); pg.wait_for_timeout(4000)
    verif('N7 « Enregistrer » partage toujours un fichier comme avant', pg.evaluate("window.__partage") >= 1 or len(telechargements) >= 1, (pg.evaluate("window.__partage"), telechargements))

    print('N8 — code refusé pendant l\'envoi')
    AZ['refus401'] = True; n_avant = len(AZ['recus'])
    pg.evaluate("c29EnvoyerTout()")
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /Carnet reçu par Azuska Z|Pas envoyé/.test(h.innerText); }", timeout=120000)
    fin = pg.inner_text('#contenuBoite')
    verif('N8 code refusé : « Pas envoyé » + la raison, rien reçu', 'Pas envoyé' in fin and "Code d'envoi incorrect" in fin and len(AZ['recus']) == n_avant, fin)
    verif('N8 les mots justes : « Azuska Z a répondu », pas de conseil « internet », pas de « .. »',
          'Azuska Z a répondu' in fin and 'internet revient' not in fin and 'pas répondu' not in fin and '..' not in fin, fin)
    AZ['refus401'] = False
    pg.evaluate("fermerBoite()")

    print('N9 — un envoi qui échoue ne fait pas croire que le carnet est sauvegardé (C2), et le dit en français (C3)')
    pg.evaluate("modifieDepuisEnregistrement = true; C.enregistre_le = '2026-11-01T08:00:00.000Z'; kyloDernierFichier = null; majEtat();")
    pg.evaluate("localStorage.setItem('kylo_adresse_azuska', 'http://127.0.0.1:9')")       # Azuska Z injoignable (réseau coupé)
    avis = []
    # ce qui s'AFFICHE vraiment dans l'avis du carnet (#avisCarnet), pas ce qu'on lui demande d'afficher
    # (l'avis « 💾 Copie du jour » du vrai « Enregistrer » de N7 peut encore être affiché : on le vide d'abord)
    pg.evaluate("(() => { const z = document.getElementById('avisCarnet'); if (z) { z.textContent = ''; z.style.display = 'none'; } })()")
    pg.evaluate("""window.__avis = []; new MutationObserver(() => { const z = document.getElementById('avisCarnet');
      if (z && z.style.display !== 'none' && window.__avis[window.__avis.length - 1] !== z.textContent) window.__avis.push(z.textContent); })
      .observe(document.body, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ['style'] });""")
    pg.evaluate("c29EnvoyerTout()")
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /Carnet reçu par Azuska Z|Pas envoyé/.test(h.innerText); }", timeout=120000)
    fin = pg.inner_text('#contenuBoite')
    etat = pg.evaluate("({ le: C.enregistre_le, modif: modifieDepuisEnregistrement, dernier: kyloDernierFichier })")
    verif('N9 réseau coupé : « Pas envoyé »', 'Pas envoyé' in fin, fin)
    verif('N9 la dernière sauvegarde reste celle d\'avant (rappel 💾 pas effacé)', etat['le'] == '2026-11-01T08:00:00.000Z' and etat['modif'] is True and etat['dernier'] is None, etat)
    garde = pg.evaluate("(() => { try { return JSON.parse(localStorage.getItem(CLE)).enregistre_le; } catch (e) { return 'illisible'; } })()")
    verif('N9 la copie gardée dans le téléphone dit aussi « pas sauvegardé »', garde == '2026-11-01T08:00:00.000Z', garde)
    N9_FIN = fin
    verif('N9 message en français, sans « Failed to fetch »', 'Azuska Z ne répond pas' in fin and not re.search(r'fail|fetch|network', fin, re.I), fin)
    verif('N9 pas de promesse fausse (« seuls les morceaux manquants »)', 'morceaux manquants' not in fin and 'repartira en entier' in fin, fin)
    verif('N9 pas d\'avis « 💾 Copie du jour » pendant l\'envoi', not any(a.startswith('💾') for a in pg.evaluate("window.__avis")), pg.evaluate("window.__avis"))
    pg.screenshot(path=os.path.join(CAPT, 'c29-echec.png'))
    pg.evaluate("fermerBoite()")
    pg.evaluate("localStorage.setItem('kylo_adresse_azuska', '%s')" % ADR_AZ)
    pg.evaluate("c29EnvoyerTout()")
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /Carnet reçu par Azuska Z|Pas envoyé/.test(h.innerText); }", timeout=120000)
    etat = pg.evaluate("({ le: C.enregistre_le, modif: modifieDepuisEnregistrement, envoye: C.c29_envoye_le })")
    verif('N9 envoi réussi : là, le carnet compte comme sauvegardé (il est sur l\'ordinateur)', etat['le'] != '2026-11-01T08:00:00.000Z' and etat['modif'] is False and etat['envoye'] == etat['le'], etat)
    pg.evaluate("fermerBoite()")

    print('N10 — porte fermée (trop de codes faux)')
    AZ['porte'] = True; n_avant = len(AZ['recus'])
    pg.evaluate("document.getElementById('avisCarnet') && (document.getElementById('avisCarnet').textContent = '')")
    pg.evaluate("c29Recevoir()"); pg.wait_for_timeout(2000)
    toast = pg.evaluate("(document.getElementById('avisCarnet') || {}).textContent || ''")
    verif('N10 recevoir : « Azuska Z a répondu : « Trop de codes faux : attends dix minutes. » »',
          toast.startswith('⚠ Azuska Z a répondu : « ' + PORTE + ' »') and '..' not in toast and 'pas répondu' not in toast and 'allumé' not in toast, toast)
    pg.evaluate("c29EnvoyerTout()")
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /Carnet reçu par Azuska Z|Pas envoyé/.test(h.innerText); }", timeout=120000)
    fin = pg.inner_text('#contenuBoite')
    verif('N10 envoyer tout : « Pas envoyé », la raison exacte, rien reçu', 'Pas envoyé' in fin and 'attends dix minutes' in fin and len(AZ['recus']) == n_avant, fin)
    verif('N10 pas « n\'a pas répondu », pas « .. », pas de conseil « internet »', 'pas répondu' not in fin and '..' not in fin and 'internet revient' not in fin and 'Rien n\'est perdu' in fin, fin)
    toast = pg.evaluate("(() => { const z = document.getElementById('avisCarnet'); return z && z.style.display !== 'none' ? z.textContent : ''; })()")
    verif('N10 pas d\'avis « 💾 Le fichier fait … » collé sous l\'avis déjà affiché (aucun fichier n\'est sorti)', '💾' not in toast, toast)
    pg.screenshot(path=os.path.join(CAPT, 'c29-porte-fermee.png'))
    AZ['porte'] = False
    pg.evaluate("fermerBoite()")
    verif('N9 réseau coupé : pas de « .. » dans le message', '..' not in N9_FIN, N9_FIN)

    verif('N1 aucune erreur JavaScript', not erreurs, erreurs)
    sonde = pg.evaluate("fetch('https://garde-reseau.invalid/sonde', { cache: 'no-store' }).then(() => 'passé', () => 'coupé')")
    verif('N0 la garde est branchée : une sonde vers une adresse hors atelier est coupée par elle', sonde == 'coupé' and any('garde-reseau.invalid' in u for u in SORTIES), (sonde, SORTIES[-3:]))
    nav.close()
vues = set(SORTIES) | set(SUR_PLACE)
hors = [u for u in TOUTES if not LOCAL.match(u)]
verif('N0 chaque demande hors atelier vue par Chromium est passée par la garde (coupée ou servie sur place)', all(u in vues for u in hors), [u for u in hors if u not in vues][:5])
verif('N0 aucune demande vers le vrai Azuska Z n\'a été coupée trop tard : l\'adresse internet est servie sur place', not any('kyloeurguine' in u for u in SORTIES), SORTIES[:5])
print('  (garde réseau : %d servie(s) sur place pour l\'adresse internet d\'Azuska Z, %d coupée(s) — %s)' % (len(SUR_PLACE), len(SORTIES), ', '.join(sorted(set(urlparse(u).netloc for u in SORTIES))) or 'aucune'))

print('\n%d/%d contrôles réussis' % (total[1], total[0]))
for e in echecs: print('ÉCHEC :', e)
sys.exit(1 if echecs else 0)
