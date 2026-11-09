#!/usr/bin/env python3
"""Carnet 1.29.0 — la VERSION EN LIGNE (https, comme https://rice117.github.io/carnet-kylo que Riche utilise).
Usage : python3 -I tests/test-carnet-1290-https.py <dossier 1.29.0> <dossier captures>
Le carnet est servi en https sur cet ordinateur ; un faux Azuska Z répond en https ; toute autre adresse est bloquée
(l'adresse internet d'Azuska Z est interceptée : rien ne sort de cet ordinateur).
Ce qu'il prouve :
  H1 onglet « Envoyer au magasin » : la carte « 📡 Par internet avec Azuska Z » est VISIBLE, hors du volet fermé
     « Envoi direct (… WiFi) », avec sa propre case pour le code d'envoi ; rien sous 14 px (contrôle C1 du 09/11) ;
  H2 taper le code dans cette case le garde, et le bandeau vert apparaît aussitôt s'il y a des fichiers de Claude ;
  H3 une vieille adresse du WiFi (http://192.168…) restée dans le téléphone : le carnet en ligne passe par l'adresse
     internet d'Azuska Z au lieu de se taire (contrôle C4 du 09/11) ;
  H4 « 📤 Envoyer tout le carnet » marche en https ; « 📥 Ajouter au carnet » aussi ;
  H5 aucune erreur JavaScript.
"""
import json, os, re, ssl, subprocess, sys, tempfile, threading, uuid
import http.server, socketserver
from urllib.parse import urlparse, parse_qs
from playwright.sync_api import sync_playwright

D1290, CAPT = sys.argv[1:3]
os.makedirs(CAPT, exist_ok=True)
PORT, PORT_AZ = 8793, 8794
TLS = tempfile.mkdtemp(prefix='tls-carnet-')
subprocess.run(['openssl', 'req', '-x509', '-newkey', 'rsa:2048', '-nodes', '-days', '2', '-subj', '/CN=127.0.0.1',
                '-keyout', os.path.join(TLS, 'k.pem'), '-out', os.path.join(TLS, 'c.pem')], check=True, capture_output=True)
CTX = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER); CTX.load_cert_chain(os.path.join(TLS, 'c.pem'), os.path.join(TLS, 'k.pem'))

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=D1290, **k)
    def end_headers(self): self.send_header('Cache-Control', 'no-store'); super().end_headers()
    def log_message(self, *a): pass

CODE = 'ABCDEF'
FICHIER = json.dumps({'format': 'kylo-import', 'v': 1, 'titre': 'Essai https', 'fournisseurs': [{'nom': 'Usine https', 'societe': 'Usine https',
    'produits': [{'ref': 'HS-%d' % k, 'prix': 5 + k, 'devise': 'CNY'} for k in range(5)]}]}).encode()
FID = uuid.uuid4().hex[:20]
AZ = {'demandes': [], 'morceaux': {}, 'recus': []}

def cors(h):
    h.send_header('Access-Control-Allow-Origin', '*'); h.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    h.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Code-Envoi'); h.send_header('Access-Control-Expose-Headers', 'Content-Length')

def repondre_az(methode, chemin, requete, code, corps):
    """Le faux Azuska Z : (statut, octets). Sert aussi pour l'adresse internet interceptée."""
    q = parse_qs(requete)
    AZ['demandes'].append((methode, chemin, code, requete))
    if re.sub(r'[^A-Z0-9]', '', (code or '').upper()) != CODE: return 401, json.dumps({'ok': False, 'erreur': "Code d'envoi incorrect."}).encode()
    if methode == 'GET' and chemin == '/api/carnet/fichiers-de-claude':
        if 'id' in q: return (200, FICHIER) if q['id'][0] == FID else (404, b'{"ok":false}')
        return 200, json.dumps({'ok': True, 'fichiers': [{'id': FID, 'nom': 'CARNET-DE-VOYAGE-IMPORT-HTTPS.json', 'titre': 'Essai https', 'taille': len(FICHIER)}]}).encode()
    if methode == 'POST' and chemin == '/api/carnet/sauvegarde':
        depot = q.get('depot', [''])[0]
        if q.get('finir') == ['1']:
            m = int(q['morceaux'][0]); parts = AZ['morceaux'].get(depot, {})
            tout = b''.join(parts[i] for i in range(m)); c = json.loads(tout.decode('utf-8'))
            AZ['recus'].append(c)
            return 200, json.dumps({'ok': True, 'message': 'Carnet reçu par Azuska Z : %d achat(s).' % len(c.get('achats', []))}).encode()
        AZ['morceaux'].setdefault(depot, {})[int(q['n'][0])] = corps
        return 200, b'{"ok":true}'
    return 404, b'{"ok":false}'

class A(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_OPTIONS(self): self.send_response(204); cors(self); self.end_headers()
    def _r(self, m):
        u = urlparse(self.path); n = int(self.headers.get('Content-Length') or 0)
        st, o = repondre_az(m, u.path, u.query, self.headers.get('X-Code-Envoi'), self.rfile.read(n) if n else b'')
        self.send_response(st); cors(self); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(o))); self.end_headers(); self.wfile.write(o)
    def do_GET(self): self._r('GET')
    def do_POST(self): self._r('POST')

socketserver.TCPServer.allow_reuse_address = True
def lancer(port, classe):
    s = socketserver.ThreadingTCPServer(('127.0.0.1', port), classe)
    s.socket = CTX.wrap_socket(s.socket, server_side=True)
    threading.Thread(target=s.serve_forever, daemon=True).start()
lancer(PORT, H); lancer(PORT_AZ, A)
URL = 'https://127.0.0.1:%d/index.html' % PORT
ADR_AZ = 'https://127.0.0.1:%d' % PORT_AZ
INTERNET = 'https://azuska.kyloeurguine.com'

total = [0, 0]; echecs = []
def verif(nom, ok, info=''):
    total[0] += 1
    if ok: total[1] += 1; print('  ✔', nom)
    else: echecs.append(nom); print('  ✘', nom, '—', str(info)[:300])

OUVERT = "window.kyloReserveLue === true"
sorties = []
def reseau(route):
    u = route.request.url
    if u.startswith('https://127.0.0.1:'): return route.continue_()
    if u.startswith(INTERNET + '/'):                       # l'adresse internet d'Azuska Z : interceptée, jamais appelée
        p = urlparse(u); r = route.request
        if r.method == 'OPTIONS': return route.fulfill(status=204, headers={'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type, X-Code-Envoi', 'Access-Control-Allow-Methods': 'POST, GET, OPTIONS'})
        st, o = repondre_az(r.method, p.path, p.query, r.headers.get('x-code-envoi'), r.post_data_buffer or b'')
        AZ['demandes'][-1] = AZ['demandes'][-1] + ('internet',)
        return route.fulfill(status=st, body=o, headers={'Access-Control-Allow-Origin': '*', 'Access-Control-Expose-Headers': 'Content-Length', 'Content-Type': 'application/json'})
    sorties.append(u); return route.abort()

with sync_playwright() as p:
    nav = p.chromium.launch()
    ctx = nav.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=1, is_mobile=True, has_touch=True, ignore_https_errors=True)
    ctx.route('**/*', reseau)
    pg = ctx.new_page(); erreurs = []
    pg.on('pageerror', lambda e: erreurs.append(str(e)))
    pg.goto(URL); pg.wait_for_function(OUVERT, timeout=60000)
    verif('H0 la page est bien servie en https', pg.evaluate("location.protocol") == 'https:')
    pg.evaluate("""(() => { C.achats = [{ id:'a1', nom:'Frontale rechargeable', quantite: 240, prix: 7, devise:'CNY' }];
      C.voyage = Object.assign(C.voyage || {}, { nom: 'Chine octobre 2026' }); sauverLocal(); })()""")

    print('H1 — la carte est visible dans la version en ligne')
    pg.evaluate("allerA('envoi')"); pg.wait_for_selector('#c29_carte', timeout=10000)
    verif('H1 le volet WiFi existe bien (version en ligne)', pg.query_selector('details.f3-direct') is not None)
    verif('H1 la carte n\'est PAS dans le volet fermé', pg.evaluate("!document.getElementById('c29_carte').closest('details')"))
    verif('H1 la carte et ses deux boutons sont visibles', pg.is_visible('#c29_carte') and all(pg.is_visible(s) for s in ['#c29_carte button.vert', '#c29_carte button.contour']))
    verif('H1 sa propre case pour le code d\'envoi, visible', pg.query_selector('#c29_code') is not None and pg.is_visible('#c29_code'))
    petit = pg.evaluate("[...document.querySelectorAll('#c29_carte, #c29_carte *')].map(e => parseFloat(getComputedStyle(e).fontSize)).filter(t => t < 14)")
    verif('H1 rien sous 14 px dans la carte', not petit, petit)
    verif('H1 la carte dit l\'adresse internet d\'Azuska Z', INTERNET in pg.inner_text('#c29_carte'), pg.inner_text('#c29_carte'))
    pg.locator('#c29_carte').scroll_into_view_if_needed(); pg.screenshot(path=os.path.join(CAPT, 'c29-https-carte.png'))

    print('H2 — taper le code')
    pg.evaluate("localStorage.setItem('kylo_adresse_azuska', '%s')" % ADR_AZ)
    pg.fill('#c29_code', 'abc-def'); pg.dispatch_event('#c29_code', 'change')
    verif('H2 le code est gardé (en majuscules)', pg.evaluate("localStorage.getItem('kylo_code_azuska')") == 'ABC-DEF')
    try: pg.wait_for_selector('#c29_bandeau', timeout=10000); vu = True
    except Exception: vu = False
    verif('H2 le bandeau vert apparaît aussitôt (1 fichier de Claude)', vu and '1 fichier pour ton carnet' in pg.inner_text('#c29_bandeau'), vu and pg.inner_text('#c29_bandeau'))
    pg.screenshot(path=os.path.join(CAPT, 'c29-https-bandeau.png'))
    pg.click('#c29_bandeau button.vert')
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /fichiers? de Claude ajouté.* sur 1/.test(h.innerText); }", timeout=60000)
    verif('H4 « Ajouter au carnet » en https : 1 sur 1', '1 fichier de Claude ajouté sur 1' in pg.inner_text('#contenuBoite'), pg.inner_text('#contenuBoite'))
    pg.evaluate("fermerBoite()")

    print('H4 — Envoyer tout en https')
    pg.evaluate("c29EnvoyerTout()")
    pg.wait_for_function("() => { const h = document.querySelector('#contenuBoite'); return h && /Carnet reçu par Azuska Z|Pas envoyé/.test(h.innerText); }", timeout=60000)
    verif('H4 « ✅ Carnet reçu par Azuska Z »', 'Carnet reçu par Azuska Z' in pg.inner_text('#contenuBoite') and AZ['recus'] and AZ['recus'][-1]['voyage']['nom'] == 'Chine octobre 2026', pg.inner_text('#contenuBoite'))
    pg.evaluate("fermerBoite()")

    print('H3 — une vieille adresse du WiFi restée dans le téléphone')
    pg.evaluate("localStorage.setItem('kylo_adresse_azuska', 'http://192.168.1.20:3000'); C.c29_recus = {}; sauverLocal();")
    n0 = len(AZ['demandes'])
    pg.reload(); pg.wait_for_function(OUVERT, timeout=60000)
    try: pg.wait_for_selector('#c29_bandeau', timeout=15000); vu = True
    except Exception: vu = False
    nouvelles = AZ['demandes'][n0:]
    verif('H3 le carnet passe par l\'adresse internet d\'Azuska Z', any(len(d) > 4 and d[4] == 'internet' and d[1] == '/api/carnet/fichiers-de-claude' for d in nouvelles), nouvelles)
    verif('H3 et le bandeau apparaît au lieu de se taire', vu)
    verif('H3 rien n\'est parti vers 192.168…', not any('192.168' in s for s in sorties), sorties)
    verif('H5 aucune erreur JavaScript', not erreurs, erreurs)
    verif('H5 aucune demande vers une autre adresse', all(s.startswith('https://127.0.0.1') or s.startswith(INTERNET) for s in sorties) or not sorties, sorties[:5])
    nav.close()

print('\n%d/%d contrôles réussis' % (total[1], total[0]))
for e in echecs: print('ÉCHEC :', e)
sys.exit(1 if echecs else 0)
