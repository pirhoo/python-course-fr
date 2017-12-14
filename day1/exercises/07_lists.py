# -*- coding: utf-8 -*-

"""
 Exercise: remplacer les espaces vides dans la phrase par des éléments du tableau.
 Pour rappel, ici parties[0] correspond à "Democratic Party".
"""

politicians = ["Barack Obama", "Hillary Clinton", "Joe Biden",
               "George W. Bush", "Donald Trump"]

parties = ["Democratic Party", "Republican Party", "Libertarian Party",
           "Green Party", "Constitution Party"]

print("After a tense race, %s from the %s is elected as President of the USA." % (politicians[0], parties[0]) )
print("After a tense race, %s from the %s is elected as President of the USA." % (politicians[4], parties[4]) )
