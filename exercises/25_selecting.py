# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "URL DES ANNONCES SUR EBAY"
# On ouvre l'autre URL et on stock le resultat dans body
body = urllib2.urlopen(base).read()
# Parse le HTML avec Beautiful Soup
soup = BeautifulSoup(body, 'html.parser')
# Liste des titres avec un selecteur CSS
titles = soup.select("SELECTEUR CSS")

for title in titles:
    # La fonction 'strip()' permet de supprimer les espaces avant et après un texte
    print title.text.strip()

"""
Tâches:
- obtenir une liste d'annonces de vélos en faisant une recherche sur ebay.fr
- les titres des annonces peuvent être trouvés avec le selecteur CSS '.lvresult h3 .vip'
"""
