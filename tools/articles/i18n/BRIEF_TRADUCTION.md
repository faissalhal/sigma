# Traduction des articles « Conseils » de SIGMA ICC (anglais et arabe)

SIGMA ICC est un bureau d'études techniques (BET) à Marrakech. Les articles français existent ; il faut les traduire
fidèlement en **anglais** (dossier `en`) ou en **arabe** (dossier `ar`) pour le site sigma-icc.ma.

## Entrée
Un fichier source Python contient une liste `ARTICLES` de dictionnaires français (`slug`, `title`, `crumb`, `desc`,
`lead`, `body`, `faq` …). Le charger ainsi :
```python
import importlib.util as u
s = u.spec_from_file_location("m", "CHEMIN_SOURCE"); m = u.module_from_spec(s); s.loader.exec_module(m)
```

## Sortie
Écrire `tools/articles/i18n/<langue>/<nom_du_fichier_source>.py` contenant UNIQUEMENT :
```python
T = {
 "conseil-xxx": {
   "title": "…", "crumb": "…", "desc": "…", "lead": "…",
   "body": """…HTML traduit…""",
   "faq": [("Question ?", "Réponse."), …],      # même nombre d'éléments que le français (0 si 0)
 },
 …
}
```
Une entrée par article du fichier source, avec exactement les mêmes slugs. Écrire le fichier au fur et à mesure
(quelques articles à la fois, en ajoutant au dictionnaire) pour ne rien perdre.

## Règles de traduction
- Traduction fidèle et naturelle, pas mot à mot : même sens, mêmes chiffres, mêmes réserves de prudence
  (« indicatif », « à confirmer par le bureau de contrôle »…). N'ajouter AUCUNE information, ne rien retirer.
- **Anglais** : anglais international clair, vouvoiement → « you ». Monnaie : garder « DH » (ex. « 3 500 DH » → « 3,500 DH »,
  séparateur de milliers à la virgule, décimales au point). Unités métriques inchangées.
- **Arabe** : arabe standard moderne clair, compréhensible au Maroc. Termes techniques courants au Maroc ; à la première
  occurrence d'un terme technique important, ajouter le terme français entre parenthèses, ex. « الخرسانة المسلحة (béton armé) »,
  « القاطع التفاضلي (différentiel) ». Chiffres en chiffres occidentaux (0-9). Monnaie : « درهم ». Garder en caractères latins
  les noms de normes et de textes : NF C 15-100, NM 06.1.100, RPS 2000, RTCM, Rokhas, ONEE, décret 2-14-499, loi 12-90…
- Noms propres et sigles : garder SIGMA ICC, Marrakech (EN : Marrakech ; AR : مراكش), Radeema, SRM, etc.
- `title` : 50 à 70 caractères en anglais si possible (l'arabe peut être un peu plus long), la requête de recherche en tête.
  `desc` : 140 à 160 caractères en anglais (arabe : 120 à 170). `crumb` : 2 à 4 mots.

## HTML : règles strictes
- Garder EXACTEMENT la même structure : mêmes balises, même ordre, même nombre de `<h2>`, `<li>`, `<tr>`, `<td>`.
  Ne traduire que le texte entre les balises.
- Les attributs `href` restent IDENTIQUES (ex. `<a href="conseil-dosage-beton-fondation-dalle.html">`). Ne jamais
  modifier une URL ni un nom de fichier.
- Ne pas mettre de guillemets triples `"""` dans le texte. Échapper correctement les apostrophes dans les chaînes Python
  (utiliser des guillemets doubles pour les chaînes qui contiennent une apostrophe).

## Validation avant de rendre la main (obligatoire)
```bash
cd /home/user/sigma && python3 - <<'EOF'
import importlib.util as u, re
def load(p, name):
    s = u.spec_from_file_location("m", p); m = u.module_from_spec(s); s.loader.exec_module(m); return getattr(m, name)
src = load("CHEMIN_SOURCE", "ARTICLES"); T = load("CHEMIN_SORTIE", "T")
assert set(T) == {a["slug"] for a in src}, "slugs différents"
for a in src:
    t = T[a["slug"]]
    for k in ("title", "crumb", "desc", "lead", "body", "faq"): assert t.get(k) is not None, (a["slug"], k)
    tags = lambda h: re.findall(r"<(/?\w+)", h)
    assert tags(t["body"]) == tags(a["body"]), ("structure HTML différente", a["slug"])
    assert re.findall(r'href="([^"]+)"', t["body"]) == re.findall(r'href="([^"]+)"', a["body"]), ("liens", a["slug"])
    assert len(t["faq"]) == len(a["faq"]), ("faq", a["slug"])
print("OK", len(T))
EOF
```
Ne modifier AUCUN autre fichier. Pas de git. À la fin, répondre en 2 lignes : nombre d'articles traduits, points délicats.
