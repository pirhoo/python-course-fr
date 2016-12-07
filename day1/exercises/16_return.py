# -*- coding: utf-8 -*-

"""
Tâches: faire une fonction qui calcule l'augmentation ou la diminution
du taux chômage entre les deux années.
"""


def get_change(unemployment_now, unemployment_then):
    # Codez votre fonction ici
    return 0

data = [
    {
        "municipality": "Ale",
        "unemployment_2009": 5.5,
        "unemployment_2014": 4.9
    },
    {
        "municipality": "Alingsås",
        "unemployment_2009": 5.7,
        "unemployment_2014": 6.0
    },
    {
        "municipality": "Alvesta",
        "unemployment_2009": 4.7,
        "unemployment_2014": 8.9
    }
]

# Stock les valeurs de deux villes dans la liste (la première et la dernière)
ale = data[0]
alvesta = data[2]
# Affiche ces valeurs
print(ale)
print(alvesta)

print(get_change(ale["unemployment_2014"], ale["unemployment_2009"]))
print(get_change(alvesta["unemployment_2014"], ale["unemployment_2009"]))
