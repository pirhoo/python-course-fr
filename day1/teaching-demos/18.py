# coding: utf-8
"""
Write a function that takes a name and a domain.
Transform the email's name to be compatible then print a complete email address.
"""


def emailify(name, domain):
    email_friendly_name = name.lower()
    email_friendly_name = email_friendly_name.replace(" ", ".")
    email_friendly_name = email_friendly_name.replace("É", "e").replace("Å", "a").replace("Ä", "a").replace("Ö", "o")
    email_friendly_name = email_friendly_name.replace("é", "e").replace("å", "a").replace("ä", "a").replace("ö", "o")

    email = email_friendly_name + "@" + domain
    print email

emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")
