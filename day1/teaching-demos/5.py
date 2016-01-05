# coding: utf-8
"""
 Exercise: calculate unemployment

"""


population = 6058.1  # in thousand
unemployed = 424.8
not_in_labor = 986.6
employed = 4646.6

employed_part = employed / population
print(employed_part * 100)  # part of employed people in percent

labor_population = population - not_in_labor
unemployment_part = unemployed / labor_population
print(unemployment_part * 100)  # port of unemployed in the working-age population
