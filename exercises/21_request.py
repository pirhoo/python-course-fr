# -*- coding: utf-8 -*-

import urllib2

# URL de la page à ouvrir
url = 'https://api.ipify.org'
# On ouvre l'URL et on stock le resultat dans response
response = urllib2.urlopen(url)
# Pour lire le contenu de la page, on utilise 'read()'
html = response.read()

"""
Tâches:
- afficher le contenu de la page dans la console
- ouvrir une autre page et afficher son contenu
"""
