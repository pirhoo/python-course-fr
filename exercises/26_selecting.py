# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

def select_text(soup, selector):
    elements = soup.select(selector)
    if len(elements) > 0:
        return elements[0].text.strip()

def select_href(soup, selector):
    elements = soup.select(selector)
    if len(elements) > 0:
        return elements[0].get('href')


base = "https://www.ebay.fr/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=v%C3%A9lo&_sacat=0"
# On ouvre l'autre URL et on stock le resultat dans body
body = urllib2.urlopen(base).read()
# Parse le HTML avec Beautiful Soup
soup = BeautifulSoup(body, 'html.parser')
# Tous les éléments de la liste
list_items = soup.select(".lvresult")

for item in list_items:
    # L'élément .lvprice contient le prix, on affiche uniquement les annonce avec un pri
    price = select_text(item, '.lvprice')
    # COMPLETEZ ICI le selecteur CSS
    title = select_text(item, '')
    # COMPLETEZ ICI le selecteur CSS
    url = select_href(item, '')

    print u"%s à %s sur %s" % (title, price, url)


"""
Tâches:
- dans chaque résultat, extraire: le titre, le prix et le lien vers l'annonce
"""
