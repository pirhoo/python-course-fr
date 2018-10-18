# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "https://www.ebay.fr/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=v%C3%A9lo&_sacat=0&_pgn="

def select_text(soup, selector):
    elements = soup.select(selector)
    if len(elements) > 0:
        return elements[0].text.strip()

def select_href(soup, selector):
    elements = soup.select(selector)
    if len(elements) > 0:
        return elements[0].get('href')

"""
Tâches:
- déplacer l'ensemble du code dans une fonction pour scrapper une page donnée
- créer une fonction pour transformer le prix en decimal (float)
"""

def clean_price(price):
    # Insérer ici le code pour nettoyer le prix
    try:
        return float(price)
    except ValueError:
        return None

def fetch_list(page = 0):
    # Déplacer le code du scrapper ici
    pass

fetch_list(0)
fetch_list(1)
fetch_list(2)
