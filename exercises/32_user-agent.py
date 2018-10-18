# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

url = "URL DE LISTE SUR LE BON COIN"

def fetch_feed(url):
    request = urllib2.Request(url, headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control': 'no-cache',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache'
    })
    body = urllib2.urlopen(request).read()
    return BeautifulSoup(body, 'html.parser')

for title in fetch_feed(url).select('span[data-qa-id=aditem_title]'):
    print title.text
