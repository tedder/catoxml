#!/usr/bin/python
# -*- coding: utf-8 -*-

#import wikipedia as pyw
from wikitools import page
from wikitools import wiki
import mwparserfromhell

print "hello world"

w = wiki.Wiki(u"http://en.wikipedia.org/w/api.php")

page = page.Page(w, title=u"User:Tedder")

print page
pagetext = page.getWikiText()
parsedPage = mwparserfromhell.parse(pagetext.decode('utf-8'))
for template in parsedPage.filter_templates():
	print template
