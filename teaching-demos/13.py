# coding: utf-8
"""
 Change title dynamically

"""

population2012 = 9500000
population2013 = 9600000
diff = population2013 - population2012

if population2013 > population2012:
    heading = "Sweden's population increases"
if population2013 < population2012:
    heading = "Sweden's population decreases"

print(heading)
