# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "https://www.ebay.fr/sch/i.html?_from=R40&_sacat=0&_nkw=v%C3%A9lo&rt=nc&LH_BIN=1&_pgn="

def select_text(soup, selector):
    elements = soup.select(selector)
    if len(elements) > 0:
        return elements[0].text.strip()

def select_href(soup, selector):
    elements = soup.select(selector)
    if len(elements) > 0:
        return elements[0].get('href')

def clean_price(price):
    price = price.lower()
    # Supprime le "EUR"
    price = price.replace('eur', '')
    # Supprime les espaces
    price = price.replace(' ', '')
    # Remplace le séparateur des décimals par un point
    price = price.replace(',', '.')
    # Retourne un float
    try:
        return float(price)
    except ValueError:
        return None

def fetch_list(page = 0):
    # On ouvre l'autre URL et on stock le resultat dans body
    body = urllib2.urlopen(base + str(page)).read()
    # Parse le HTML avec Beautiful Soup
    soup = BeautifulSoup(body, 'html.parser')
    # Tous les éléments de la liste
    list_items = soup.select(".lvresult")

    for item in list_items:
        # L'élément .lvprice contient le prix, on affiche uniquement les annonce avec un pri
        price = select_text(item, '.lvprice')
        price = clean_price(price)
        title = select_text(item, '.lvtitle .vip')
        url = select_href(item, '.lvtitle .vip')

        print u"%s à %s sur %s" % (title, price, url)

"""
Tâches:
- créez une boucle FOR qui va afficher les annonces sur au moins 3 pages
"""

fetch_list()
