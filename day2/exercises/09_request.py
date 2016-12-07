# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "https://www.leboncoin.fr/velos/offres/ile_de_france/paris/?location=Paris&o="

def fetch_ad(url):
    pass

def fetch_list(page = 1):
    # On ouvre l'autre URL et on stock le resultat dans body
    body = urllib2.urlopen(base + str(page)).read()
    # Parse le HTML avec Beautiful Soup
    soup = BeautifulSoup(body, 'html.parser')
    # Tous les éléments de la liste
    for list_item in soup.select(".list_item"):
        # Seulement les annonces avec un prix
        if list_item.section.h3 != None:
            url = list_item['href']
            # L'URL sur Le Bon Coin ne contient pas le protocol
            url = url if url.startswith("http") else "http:%s" % url
            # On affiche dans la console la procédure en cours
            print u"Téléchargement de %s" % url
            # On appelle ici l'autre fonction pour télécharger une annonce
            fetch_ad(url)

fetch_list(1)

"""
Tâches:
- pour chaque item, ouvrir l'annonce correspondante
- extraire la valeur de '.line.properties_description' l'annonce
"""
