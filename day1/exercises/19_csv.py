# -*- coding: utf-8 -*-
import csv

# On ouvre le fichier comme du texte
in_file = open("./goodiebag/unemployment.csv", 'rb')
# On interprête ce fichier comme un CSV
csv_file = csv.DictReader(in_file, delimiter=';')

"""
Tâches: convertissez en décimal les propriétés "unemployment_2009" et "unemployment_2014"
à partir du texte en utilisant la fonction float().
"""

# On parcout le fichier ligne par ligne
for row in csv_file:
    print("Orignal data:")
    print(row)
    # Codez ici!
    print(row)
