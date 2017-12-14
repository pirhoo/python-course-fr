# -*- coding: utf-8 -*-
import csv

# On ouvre le fichier comme du texte
in_file = open("./goodiebag/unemployment.csv", 'rb')
# On interprête ce fichier comme un CSV
csv_file = csv.DictReader(in_file, delimiter=';')

"""
Tâche: comptez le nombre de lignes présentes dans ce fichier CSV.
"""

counter = 0
# On parcout le fichier ligne par ligne
for row in csv_file:
    print(row)

print(u"Il y a %s lignes dans ce fichier CSV!" % counter)
