# -*- coding: utf-8 -*-

name = "Clémentine Autain"
domain = "riksdagen.se"

"""
Tâches:
- Utilisez .replace() pour remplace les espaces par des points et les "é" par des "e"
- Utilisez .lower() pour passer le texte en minuscule
"""

name = name.lower()
name = name.replace(" ", ".").replace("é", "e")
email = ("%s@%s") % (name, domain)
print(email)
