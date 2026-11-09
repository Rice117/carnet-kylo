# -*- coding: utf-8 -*-
"""Carnet 1.28.0 — les dépenses du voyage arrivent par le fichier de Claude (frais[] dans kylo-import).
Lancer :  python3 tests/test-carnet-1280.py [chemin du fichier KYLO-import-depenses…json]
Sert le dossier du carnet en local, ouvre le carnet taille téléphone, ajoute le fichier, vérifie."""
import json, os, sys, threading, http.server, socketserver, functools
from playwright.sync_api import sync_playwright

ICI = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(ICI)
FICHIER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ICI, 'exemple-frais-1280.json')
PORT = 8765
OK = []; KO = []
def verif(nom, cond, detail=''):
    (OK if cond else KO).append(nom); print(('✅ ' if cond else '❌ ') + nom + (' — ' + str(detail) if detail and not cond else ''))

class Silencieux(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
Handler = functools.partial(Silencieux, directory=RACINE)
socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.TCPServer(('127.0.0.1', PORT), Handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()

if not os.path.exists(FICHIER):
    json.dump({"format": "kylo-import", "titre": "essai", "fournisseurs": [], "frais": [
        {"cle": "alipay:2026-10-19:09:40", "libelle": "Hôtel — essai", "montant": 234.84, "devise": "CNY", "date": "2026-10-19", "mode": "alipay", "repartition": "valeur"},
        {"cle": "alipay:2026-11-05:12:33", "libelle": "Matériel du magasin — caméras", "montant": 1802.5, "devise": "CNY", "date": "2026-11-05", "mode": "alipay", "repartition": "aucune"},
        {"cle": "dit:especes", "libelle": "Espèces", "montant": 1400, "devise": "EUR", "date": "2026-10-19", "mode": "especes"},
        {"libelle": "", "montant": 5}, {"libelle": "sans montant"}]}, open(FICHIER, 'w'), ensure_ascii=False)
imp = json.load(open(FICHIER, encoding='utf-8'))
attendu = [f for f in imp['frais'] if str(f.get('libelle', '')).strip() and float(f.get('montant') or 0) > 0]
tot_cny = round(sum(float(f['montant']) for f in attendu if f.get('devise', 'CNY') == 'CNY'), 2)
tot_eur = round(sum(float(f['montant']) for f in attendu if f.get('devise') == 'EUR'), 2)
texte = json.dumps(imp, ensure_ascii=False)

with sync_playwright() as p:
    nav = p.chromium.launch()
    ctx = nav.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    page = ctx.new_page()
    erreurs = []; page.on('pageerror', lambda e: erreurs.append(str(e)))
    page.goto(f'http://127.0.0.1:{PORT}/index.html'); page.wait_for_timeout(1500)
    verif('1. le carnet est en 1.28.0', page.evaluate('window.KYLO_APPLICATION') == '1.28.0', page.evaluate('window.KYLO_APPLICATION'))
    verif('2. le module frais est chargé', page.evaluate('window.KYLO_FRAIS_FICHIER') == '1.28.0')
    # taux : 1 € = 8,58 ¥ ; GNF via le carnet (on fixe CNY et EUR en GNF)
    page.evaluate("() => { C.voyage.taux = C.voyage.taux || {}; C.voyage.taux.CNY = 1200; C.voyage.taux.EUR = 10296; C.voyage.devise = 'CNY'; sauverLocal(); }")
    n0 = page.evaluate('(C.frais||[]).length')
    # un frais tapé à la main avant, pour vérifier qu'il reste
    page.evaluate("() => { C.frais.push({ id: idUnique('f'), libelle: 'Repas tapé à la main', montant: 50, devise: 'CNY', repartition: 'valeur', produit_id: '', note: '', date: '2026-10-20', etat: 'paye' }); sauverLocal(); }")
    # ouvrir la boîte, coller le fichier, aperçu
    page.evaluate("ctBoiteImport('')"); page.wait_for_timeout(300)
    page.evaluate("(t) => { const z = document.getElementById('ct_code'); z.value = t; delete z.dataset.fichier; }", texte)
    page.evaluate("ctApercuImport()"); page.wait_for_timeout(1500)
    apercu = page.inner_text('#ct_apercu_import')
    verif('3. l’aperçu annonce le bon nombre de dépenses', f"{len(attendu)} dépense" in apercu, apercu[:200])
    verif('4. l’aperçu donne le total en yuans', ('%s' % f"{tot_cny:,.2f}".replace(',', ' ').replace('.', ',')).split(',')[0] in apercu.replace(' ', ' ').replace('\xa0', ' ') or str(int(tot_cny)) in apercu.replace(' ', '').replace(' ', '').replace('\xa0', ''), apercu[:300])
    verif('5. le bouton Ajouter est actif', page.evaluate("!document.getElementById('ct_bouton_import').disabled"))
    page.screenshot(path=os.path.join(ICI, 'capture-1280-apercu.png'))
    page.evaluate("ctAppliquerImport()"); page.wait_for_timeout(1500)
    n1 = page.evaluate('(C.frais||[]).length')
    verif('6. toutes les dépenses sont ajoutées (+ la ligne tapée à la main gardée)', n1 == n0 + 1 + len(attendu), (n0, n1, len(attendu)))
    verif('7. le carnet s’ouvre sur l’onglet Frais', page.evaluate('ongletActif') == 'frais', page.evaluate('ongletActif'))
    ecran = page.inner_text('#ecran') if page.query_selector('#ecran') else page.inner_text('body')
    verif('8. la première dépense est visible à l’écran', attendu[0]['libelle'][:18] in ecran, attendu[0]['libelle'])
    verif('9. le matériel est « hors coût des produits »', page.evaluate("(C.frais||[]).filter(f => f.cle_import && f.repartition === 'aucune').length") == len([f for f in attendu if f.get('repartition') == 'aucune']))
    verif('10. le mode Alipay est gardé', page.evaluate("(C.frais||[]).filter(f => f.cle_import && f.mode === 'alipay').length") == len([f for f in attendu if f.get('mode') == 'alipay']))
    verif('11. le total des frais ajoutés en ¥ est juste', abs(page.evaluate("(C.frais||[]).filter(f => f.cle_import && f.devise === 'CNY').reduce((s, f) => s + f.montant, 0)") - tot_cny) < 0.01)
    verif('12. le total des frais ajoutés en € est juste', abs(page.evaluate("(C.frais||[]).filter(f => f.cle_import && f.devise === 'EUR').reduce((s, f) => s + f.montant, 0)") - tot_eur) < 0.01)
    verif('13. l’argent sorti (f2Sorties) compte les nouvelles dépenses', page.evaluate("typeof f2Sorties === 'function' ? f2Sorties().filter(s => s.source === 'frais' && s.mode === 'alipay').length : -1") == len([f for f in attendu if f.get('mode') == 'alipay']))
    page.screenshot(path=os.path.join(ICI, 'capture-1280-frais.png'), full_page=False)
    # rejouer le MÊME fichier : rien en double
    page.evaluate("ctBoiteImport('')"); page.wait_for_timeout(300)
    page.evaluate("(t) => { const z = document.getElementById('ct_code'); z.value = t; delete z.dataset.fichier; }", texte)
    page.evaluate("ctApercuImport()"); page.wait_for_timeout(1200)
    apercu2 = page.inner_text('#ct_apercu_import')
    verif('14. l’aperçu dit que tout est déjà présent', f"{len(attendu)} déjà présente" in apercu2, apercu2[:200])
    verif('15. le bouton Ajouter reste inactif quand rien n’est nouveau', page.evaluate("document.getElementById('ct_bouton_import').disabled"))
    page.evaluate("ctAppliquerImport()"); page.wait_for_timeout(800)
    verif('16. rien en double après le second ajout', page.evaluate('(C.frais||[]).length') == n1)
    # supprimer une dépense venue du fichier (deux appuis) : elle ne revient pas
    idf = page.evaluate("(C.frais||[]).find(f => f.cle_import).id")
    page.evaluate("(i) => { supprimerFrais(i); supprimerFrais(i); }", idf); page.wait_for_timeout(300)
    verif('17. la dépense supprimée a disparu', page.evaluate("(i) => !(C.frais||[]).some(f => f.id === i)", idf))
    page.evaluate("ctBoiteImport('')"); page.wait_for_timeout(300)
    page.evaluate("(t) => { const z = document.getElementById('ct_code'); z.value = t; delete z.dataset.fichier; }", texte)
    page.evaluate("ctApercuImport()"); page.wait_for_timeout(1200); page.evaluate("ctAppliquerImport()"); page.wait_for_timeout(800)
    verif('18. une dépense supprimée à la main ne revient pas avec le fichier', page.evaluate('(C.frais||[]).length') == n1 - 1)
    # un fichier SANS frais passe par l’ancien chemin
    page.evaluate("ctBoiteImport('')"); page.wait_for_timeout(300)
    sans = json.dumps({"format": "kylo-import", "titre": "sans frais", "fournisseurs": [{"nom": "Essai Fournisseur 1280", "code": "Y99", "produits": []}]})
    page.evaluate("(t) => { const z = document.getElementById('ct_code'); z.value = t; delete z.dataset.fichier; }", sans)
    page.evaluate("ctApercuImport()"); page.wait_for_timeout(1200)
    verif('19. un fichier sans frais garde l’ancien aperçu (fournisseur)', 'Essai Fournisseur 1280' in page.inner_text('#ct_apercu_import'))
    page.evaluate("ctAppliquerImport()"); page.wait_for_timeout(1500)
    verif('20. le fournisseur est ajouté comme avant', page.evaluate("fournisseursListe().some(f => String(f.nom||f.societe||'').includes('Essai Fournisseur 1280'))"))
    # fichier mixte : frais + fournisseur
    page.evaluate("ctBoiteImport('')"); page.wait_for_timeout(300)
    mixte = json.dumps({"format": "kylo-import", "fournisseurs": [{"nom": "Essai Fournisseur 1281", "code": "Y98", "produits": []}],
                        "frais": [{"cle": "mixte:1", "libelle": "Taxi mixte", "montant": 12, "devise": "CNY", "date": "2026-11-01"}]})
    page.evaluate("(t) => { const z = document.getElementById('ct_code'); z.value = t; delete z.dataset.fichier; }", mixte)
    page.evaluate("ctApercuImport()"); page.wait_for_timeout(1200); page.evaluate("ctAppliquerImport()"); page.wait_for_timeout(1500)
    verif('21. fichier mixte : le frais ET le fournisseur sont ajoutés', page.evaluate("(C.frais||[]).some(f => f.cle_import === 'mixte:1') && fournisseursListe().some(f => String(f.nom||'').includes('Essai Fournisseur 1281'))"))
    # relecture après rechargement : tout est resté
    page.reload(); page.wait_for_timeout(1500)
    verif('22. après rechargement, les dépenses sont toujours là', page.evaluate("(C.frais||[]).filter(f => f.cle_import).length") == len(attendu) - 1 + 1)
    verif('23. aucune erreur JavaScript', not erreurs, erreurs[:3])
    nav.close()
srv.shutdown()
print(f"\n{len(OK)} bons, {len(KO)} mauvais" + (' : ' + ', '.join(KO) if KO else ''))
sys.exit(1 if KO else 0)
