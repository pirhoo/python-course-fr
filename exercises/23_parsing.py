# -*- coding: utf-8 -*-

import urllib2
# Si BeautifulSoup n'est pas installé: pip install beautifulsoup4
from bs4 import BeautifulSoup

# L'URL pour trouver le pays correspondant à une ip ou un nom de domaine
infourl = 'http://ip-api.com/xml/pirhoo.com'
# On ouvre l'autre URL et on stock le resultat dans response
infobody = urllib2.urlopen(infourl).read()
# Ce resultat est au format XML (comme du HTML),
# il faut que Python puisse le comprendre
soup = BeautifulSoup(infobody, 'html.parser')
# Affiche des valeur
print u"Pays: %s" % soup.response.countryname.text

"""
Tâches:
- changer le site (ou l'ip) cible
- afficher d'autre information dans la console avec xpath
"""
