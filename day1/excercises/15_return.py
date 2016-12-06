# -*- coding: utf-8 -*-

"""
Tâches: faire une fonction qui prend un pourcentage de chômage et retorune une
catégrie comme "faible", "moyen" ou "élevé" à l'aide d'une condition IF.
"""


def categorize_unemployment(unemployment):
    if unemployment < 5.0:
        return "faible"

print(categorize_unemployment(1.2))
print(categorize_unemployment(10.3))
print(categorize_unemployment(7.8))
print(categorize_unemployment(5.6))
print(categorize_unemployment(2.1))
