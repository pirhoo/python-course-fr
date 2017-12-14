# -*- coding: utf-8 -*-

politicians = [
    "Marie-Do AESCHLIMANN",
    "Samira AIDOUD",
    "Magali ALEXANDRE",
    "Mathilde ANDROUËT",
    "Clémentine AUTAIN",
    "Nadège AZZAZ",
    "Marie-Pierre BADRÉ",
    "Charlotte BAELDE"
]

"""
Tâches:
Utilisez la fonction len(), qui s'applique aux chaînes et aux listes,
afin de déterminer combien de politicien ont des noms longs ou courts.
"""

long_names = 0
short_names = 0
total_names = len(politicians)

print("Nos compteurs ont été mis à 0")

for name in politicians:
    print("La boucle est exécutée ici")

print("%s sur %s politiciens ont un nom long." % (long_names, total_names))
print("%s sur %s politiciens ont un nom courts." % (short_names, total_names))
