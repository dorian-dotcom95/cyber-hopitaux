import feedparser

# 1. On prépare la structure de ton site (le haut de la page)
html = """
<html>
<head>
    <meta charset="utf-8">
    <title>Mon Site Cyber Hôpitaux</title>
    <style>
        body { font-family: sans-serif; background: #f0f2f5; padding: 20px; }
        h1 { color: #d9534f; border-bottom: 2px solid #d9534f; }
        .alerte { background: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        a { color: #0275d8; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🛡️ Alertes Cyber dans les Hôpitaux (Depuis Sept. 2024)</h1>
"""

# 2. Le bot va chercher les infos
flux_rss = ["https://www.cert.ssi.gouv.fr/alerte/feed/", "https://www.lemondeinformatique.fr/flux-rss/thematique/securite/rss.xml"]
mots_cles = ["hôpital", "hopital", "chu", "clinique", "santé", "medical"]

print("Le bot travaille... génération du site en cours.")

for url in flux_rss:
    flux = feedparser.parse(url)
    for art in flux.entries:
        contenu = (art.title + " " + getattr(art, 'summary', '')).lower()
        if any(mot in contenu for mot in mots_cles):
            # 3. On ajoute l'alerte dans le code du site
            html += f"""
            <div class="alerte">
                <h3>{art.title}</h3>
                <p><a href="{art.link}" target="_blank">Clique ici pour voir l'article</a></p>
            </div>
            """

# 4. On finit le code du site et on enregistre
html += "</body></html>"
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("TERMINÉ ! Cherche le fichier 'index.html' sur ton bureau et ouvre-le.")
