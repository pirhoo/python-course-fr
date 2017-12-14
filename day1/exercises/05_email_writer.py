# -*- coding: utf-8 -*-
"""
Écrire une fonction qui prend pour paramète un nom et un domaine.
Transformez le nom pour être avec une adresse email et affichez le.
"""


def emailify(name, domain):
    """
     Ce code doit:
     1) remplacer les epsaces par des "."
     2) convertir en minuscule
     3) remplacer les caractères spéciaux (é, è, ë) par des caractères non-accentués
     4) afficher le resutat
     5) retourner le resutat
    """
    name = name.replace(" ", ".")
    name = name.lower()
    name = name.replace('é', 'e')
    name = name.replace('è', 'e')
    name = name.replace('ë', 'e')

    print ("%s@%s") % (name, domain)


emailify("Mathilde ANDROUËT", "iledefrance.fr")
emailify("Clémentine AUTAIN", "iledefrance.fr")
emailify("Nadège AZZAZ", "iledefrance.fr")
emailify("Marie-Pierre BADRÉ", "iledefrance.fr")
emailify("Charlotte BAELDE", "iledefrance.fr")
