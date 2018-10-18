# -*- coding: utf-8 -*-

import urllib2
import re
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "https://www.ebay.fr/sch/i.html?_from=R40&_sacat=0&_nkw=v%C3%A9lo&rt=nc&LH_BIN=1&_pgn="
ads = []

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

def fetch_ad(url):
    # On ouvre l'autre URL et on stock le resultat dans body
    body = urllib2.urlopen(url).read()
    # Parse le HTML avec Beautiful Soup
    return BeautifulSoup(body, 'html.parser')

def fetch_list(page = 0):
    # On ouvre l'autre URL et on stock le resultat dans body
    body = urllib2.urlopen(base + str(page)).read()
    # Parse le HTML avec Beautiful Soup
    soup = BeautifulSoup(body, 'html.parser')
    # Tous les éléments de la liste
    list_items = soup.select(".lvresult")

    for item in list_items[0:10]:
        url = select_href(item, '.lvtitle .vip')
        ad = fetch_ad(url)

        ads.append({
            "price": clean_price(select_text(item, '.lvprice')),
            "title": select_text(item, '.lvtitle .vip'),
            "url": url,
            "seller": select_text(ad, '..mbg-nw'),
            "description": select_text(ad, '.bsi-cnt')
        })

# Toutes les annonces de la page 1 sont stockées dans la liste "ads"
fetch_list(1)
# Parcours la liste des annonces
for ad in ads:
    # Trouve toute les occurences de la regex pour trouver un numéro de téléphone
    matches = re.search('\d{10}', ad['description'])
    # Si matches n'est pas None, ça veut dire qu'on a trouvé des occurences
    if matches is not None:
        print matches.group(0)

# On affiche le resultat au format CSV
writer = UnicodeWriter(open("./ads.csv", 'w'), fieldnames=['price', 'title', 'url', 'seller'])
# Ajoute toutes les lignes une par une
( writer.writerow(ad) for ad in ads  )
