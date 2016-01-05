# coding: utf-8
"""
 Exercise: display unemployment

"""


population = 6058.1  # in thousand
unemployed = 424.8
not_in_labor = 986.6
employed = 4646.6

employed_part = employed / population
unemployment_part = unemployed / (population - not_in_labor)

print("The percentage of employed is %s percent and unemployment %s percent" % (employed_part * 100, unemployment_part * 100) )
