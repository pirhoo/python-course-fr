# encoding: utf-8

import csv

in_file = open("unemployment.csv", 'rb')
rows = csv.DictReader(in_file, delimiter=';')

for row in rows:
    print(row['unemployment_2009'])