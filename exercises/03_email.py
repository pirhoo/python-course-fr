# -*- coding: utf-8 -*-

first_name = "clementine"
last_name = "autain"
domain = "iledefrance.fr"

"""
Tâches:
- Créez une variable combinant ces 3 éléments pour créer un email
- Afficher cet email
"""

# Method 1
email = first_name + "." + last_name + "@" + domain
print(email)

# Method 2
email = "%s.%s@%s" % (first_name, last_name, domain)
print(email)
