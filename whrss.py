#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import urlopen
from dateutil.parser import parse as parse_date

def get_item(e):
    created = parse_date(e.select('.views-field-created')[0].text)
    created = created.strftime("%a, %d %b %Y %H:%M:%S +0000")
    a = e.select('a')[0]
    url = 'https://www.whitehouse.gov' + a['href']

    # ignore links to this page which changes every day and isn't a permalink
    if url == "https://www.whitehouse.gov/1600daily":
        return None

    title = a.text
    return """<item><title>%s</title><link>%s</link><guid>%s</guid><description>%s</description><pubDate>%s</pubDate></item>""" % (title, url, url, title, created)

html = urlopen("https://www.whitehouse.gov/blog").read()
doc = BeautifulSoup(html, "html.parser")

print("""<?xml version="1.0" encoding="utf-8" ?><rss version="2.0" xml:base="https://www.whitehouse.gov/blog-daily-listings-rss" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>White House - What's Happening</title><link>https://www.whitehouse.gov/blog-daily-listings-rss</link><description></description><language>en</language><atom:link href="https://inkdroid.org/rss/whitehouse.xml" rel="self" type="application/rss+xml" />""", end="") 

for e in doc.select('.views-row'):
    item = get_item(e)
    if item:
        print(item, end="")

print("</channel></rss>", end="")
