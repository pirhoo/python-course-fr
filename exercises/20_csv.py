# -*- coding: utf-8 -*-
import csv

# On ouvre le fichier comme du texte
in_file = open("../goodiebag/unemployment.csv", 'rt')
# On interprête ce fichier comme un CSV
csv_file = csv.DictReader(in_file, delimiter=';')

"""
Tâches: utilisez la fonction que vous avez écrit à l'exercice 5 pour afficher
une histoire sur le taux de chômage de chaque des villes.
"""

def write_story(municipality, unemployment_2009, unemployment_2014):
    story = u"Voici quelques info sur le taux de chomage à %s" % municipality
    # Codez ici
    return story

# On parcout le fichier ligne par ligne
for row in csv_file:
    print("*****")
    municipality = row["municipality"].decode("utf-8")
    # On convertit les valeurs en décimal
    unemployment_2009 = float(row["unemployment_2009"])
    unemployment_2014 = float(row["unemployment_2014"])
    # On appelle la fonction pour écrire une histoire avec nos valeurs
    story = write_story(municipality, unemployment_2009, unemployment_2014)

    print(story)
