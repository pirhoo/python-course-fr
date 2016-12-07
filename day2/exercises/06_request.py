# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "https://www.leboncoin.fr/velos/offres/ile_de_france/paris/?location=Paris&o="
# On ouvre l'autre URL et on stock le resultat dans body
body = urllib2.urlopen(base).read()
# Parse le HTML avec Beautiful Soup
soup = BeautifulSoup(body, 'html.parser')
# Tous les éléments de la liste
list_items = soup.select(".list_item")

for list_item in list_items:
    # L'élément h3 contient le prix, on affiche uniquement les annonce avec un pri
    if list_item.section.h3 != None:
        print u"%s à %s sur %s" % (None, None, None)


"""
Tâches:
- dans chaque résultat, extraire: le titre, le prix et le lien vers l'annonce
"""
