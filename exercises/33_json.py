import json
import urllib2

def fetch_recipes():
    url = "TROUVER L'URL DE L'API SUR http://www.recipepuppy.com POUR DES RAMENS"
    return urllib2.urlopen(url).read()

body = json.loads(fetch_recipes())

for recipe in body["results"]:
    # Afficher ici le titre et le lien de chaque recette
