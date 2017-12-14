# -*- coding: utf-8 -*-

"""
Voir 06_robot_writer.md pour les consignes
"""

total_unemployment_2009 = 8.8
total_unemployment_2016 = 9.6

def write_story(municipality, unemployment_2009, unemployment_2016):
    unemployment_diff = unemployment_2016 - unemployment_2009
    total_unemployment_diff = total_unemployment_2016 - total_unemployment_2009
    if unemployment_2016 > unemployment_2009:
        print("In 2014, unemployment in %s was %s higher than before the financial crisis in 2009." % (municipality, unemployment_diff))
        print("It increased from %s%% to %s%%." % (unemployment_2009, unemployment_2016))
    else:
        print("In 2014, unemployment in %s was %s lower than before the financial crisis in 2009." % (municipality, -unemployment_diff))
        print("It decreased from %s%% to %s%%." % (unemployment_2009, unemployment_2016))
    if unemployment_diff > total_unemployment_diff:
        print("The development of this city has been a little worse than in the country where the unemployment rate during the same period grew by %s" % total_unemployment_diff)
    else:
        print("The development of this city has been a little better than in the country where the unemployment rate during the same period grew by %s" % total_unemployment_diff)

"""
Tests du robot!
Source: https://www.insee.fr/fr/statistiques/1893230
"""


write_story("Lyon", 8.3, 8.8)
print '*****************'
write_story("Marseille", 11.5, 12.1)
print '*****************'
write_story("Paris", 7.8, 8.4)
print '*****************'
write_story("Saint-Nazaire", 8.4, 8.7)
print '*****************'
write_story("Tours", 7.8, 9.1)
