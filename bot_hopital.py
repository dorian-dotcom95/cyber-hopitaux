import feedparser
import urllib.parse

# 1. On prépare la structure du site
html = """
<html>
<head>
    <meta charset="utf-8">
    <title>Observatoire Cyber Médical</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f4f7f6; padding: 30px; }
        h1 { color: #2c3e50; border-bottom: 3px solid #e74c3c; padding-bottom: 10px; }
        .alerte { background: white; padding: 20px; margin-bottom: 15px; border-radius: 10px; border-left: 8px solid #e74c3c; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .date { color: #7f8c8d; font-size: 0.9em; font-weight: bold; }
        h3 { margin-top: 5px; color: #c0392b; }
        a { color: #2980b9; text-decoration: none; font-weight: bold; }
        .vide { text-align: center; padding: 50px; color: #7f8c8d; font-style: italic; }
    </style>
</head>
<body>
    <h1>🛡️ Alertes Cyber dans les Hôpitaux (Depuis Sept. 2024)</h1>
"""

# 2. Utilisation de Google News pour avoir des archives plus larges
# On cherche "cyberattaque hopital" depuis le 01/09/2024
query = urllib.parse.quote('cyberattaque hopital after:2024-09-01')
url_google = f"https://news.google.com/rss/search?q={query}&hl=fr&gl=FR&ceid=FR:fr"

print("Recherche des archives en cours...")
flux = feedparser.parse(url_google)

if len(flux.entries) == 0:
    html += "<div class='vide'>Aucune alerte trouvée pour le moment. Réessayez plus tard.</div>"
else:
    for art in flux.entries:
        # On affiche chaque article trouvé par Google News
        html += f"""
        <div class="alerte">
            <div class="date">Publié le : {art.published}</div>
            <h3>{art.title}</h3>
            <p><a href="{art.link}" target="_blank">👉 Lire l'article complet</a></p>
        </div>
        """

html += "</body></html>"

# 3. Enregistrement
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"TERMINÉ ! {len(flux.entries)} articles ajoutés.")
