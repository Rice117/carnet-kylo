#!/usr/bin/env python3
"""Carnet 1.29.1 — la copie légère (sans les photos) quand la copie fait plus de 120 Mo.
Usage : python3 -I tests/test-carnet-1291.py <dossier 1.29.1>
  L1 c29Alleger retire chaque photo « data:image… » et rien d'autre : le JSON obtenu est exactement le carnet sans photos
     (photos à cheval sur deux tranches de 8 Mo, marque coupée par une tranche, accents à cheval, guillemet échappé) ;
  L2 une copie de 130 Mo (au-dessus de la limite) devient une copie légère de moins de 1 Mo ;
  L3 rien ne sort de l'atelier (garde réseau)."""
import sys, os, threading, http.server, functools, re
from playwright.sync_api import sync_playwright
D = os.path.abspath(sys.argv[1]); ok = 0; ko = 0
def verif(nom, cond, detail=''):
    global ok, ko
    if cond: ok += 1; print('  ✔', nom)
    else: ko += 1; print('  ✘', nom, '—', str(detail)[:300])
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(H, directory=D)); threading.Thread(target=srv.serve_forever, daemon=True).start()
SORTIES = []
def garde(route):
    u = route.request.url
    if re.match(r'^(http://127\.0\.0\.1:|data:|blob:)', u): return route.continue_()
    SORTIES.append(u); return route.abort()
JS = r"""async (mo) => {
  const T = 8 * 1024 * 1024, photo = n => 'data:image/jpeg;base64,' + 'A'.repeat(n);
  const c = { format: 'kylo-carnet-achats', voyage: { nom: 'Été à Yiwu — é'.repeat(3) }, achats: [], fournisseurs: [] };
  // de quoi faire tomber des photos, la marque et des accents sur les coupes de 8 Mo
  let taille = 0;
  for (let i = 0; taille < mo * 1048576; i++) {
    const n = i % 3 === 0 ? 3 * 1024 * 1024 + i * 7 : 500000 + i * 13;
    c.achats.push({ nom: 'Produit é' + i, photo: photo(n), note: 'il a dit \"data:image/ pas une photo\" — ok', prix: i });
    c.fournisseurs.push({ nom: 'F' + i, tel: '13' + i, carte: photo(1000 + i), produits: [{ ref: 'R' + i, photo: photo(200 + i) }] });
    taille += n + 1500;
  }
  const texte = JSON.stringify(c);
  // remplir pour que la marque « "data:image/ » tombe pile sur une coupe
  const attendu = JSON.parse(texte, (k, v) => typeof v === 'string' && v.startsWith('data:image/') ? '' : v);
  const blob = new Blob([texte]);
  const leger = await c29Alleger(blob);
  let obtenu = null, erreur = '';
  try { obtenu = JSON.parse(await leger.text()); } catch (e) { erreur = String(e); }
  return { avant: blob.size, apres: leger.size, photos: leger.c29Photos, attendues: c.achats.length + c.fournisseurs.length * 2,
           pareil: obtenu !== null && JSON.stringify(obtenu) === JSON.stringify(attendu), erreur };
}"""
with sync_playwright() as p:
    nav = p.chromium.launch(); ctx = nav.new_context(viewport={'width': 390, 'height': 844}); ctx.route('**/*', garde)
    pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('http://127.0.0.1:%d/index.html' % srv.server_address[1]); pg.wait_for_function("typeof c29Alleger === 'function'", timeout=60000)
    verif('L0 version 1.29.1', pg.evaluate("window.KYLO_APPLICATION") == '1.29.1')
    r = pg.evaluate(JS, 40)
    verif('L1 copie de 40 Mo : le carnet sans photos, exactement (%d photos retirées)' % r['photos'], r['pareil'] and r['photos'] == r['attendues'], r)
    r = pg.evaluate(JS, 130)
    verif('L2 copie de %d Mo (au-dessus de 120 Mo) → copie légère de %d Ko, JSON exact' % (r['avant'] // 1048576, r['apres'] // 1024), r['pareil'] and r['avant'] > 120 * 1048576 and r['apres'] < 1048576, r)
    verif('L1 aucune erreur JavaScript', not errs, errs)
    nav.close()
verif('L3 rien ne sort de l\'atelier', not any('kyloeurguine' in u for u in SORTIES), SORTIES[:3])
print('\n%d contrôles réussis, %d en échec' % (ok, ko)); sys.exit(1 if ko else 0)
