# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "https://www.leboncoin.fr/velos/offres/ile_de_france/paris/?location=Paris&o="

def fetch_list(page = 1):
    # On ouvre l'autre URL et on stock le resultat dans body
    body = urllib2.urlopen(base + str(page)).read()
    # Parse le HTML avec Beautiful Soup
    soup = BeautifulSoup(body, 'html.parser')
    # Tous les éléments de la liste
    list_items = soup.select(".list_item")

    for list_item in list_items:
        if list_item.section.h3 != None:
            print u"%s à %s sur %s" % (
                list_item['title'],
                list_item.section.h3.text.strip(),
                list_item['href']
            )

"""
Tâches:
- créez une boucle FOR qui va afficher les annonces sur au moins 3 pages
"""
