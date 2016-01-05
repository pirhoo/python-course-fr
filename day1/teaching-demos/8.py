# coding: utf-8
"""
 Exercise: write an email

"""

first_name = "gustaf"
last_name = "fridolin"
domain = "riksdagen.se"

email = first_name + "." + last_name + "@" + domain
print(email)

# Alternative: string replacement
email = "%s.%s@%s" % (first_name, last_name, domain)
