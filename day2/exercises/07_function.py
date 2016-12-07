# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

base = "https://www.leboncoin.fr/velos/offres/ile_de_france/paris/?location=Paris&o="

def fetch_list(page = 1):
    # Déplacer le code du scrapper ici
    pass

fetch_list(1)
fetch_list(2)
fetch_list(3)

"""
Tâches:
- déplacer l'ensemble du code dans une fonction pour scrapper une page donnée
"""
