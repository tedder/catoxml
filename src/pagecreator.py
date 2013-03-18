#!/usr/bin/python
# -*- coding: utf-8 -*-

#import wikipedia as pyw
from wikitools import page
from wikitools import wiki
import mwparserfromhell
import sys

print "hello world"

parsedPage = mwparserfromhell.parse("".decode('utf-8'))

for line in sys.stdin:
	parsedPage.append("* ")
	parsedPage.append(mwparserfromhell.nodes.wikilink.Wikilink(line.rstrip()))
	parsedPage.append("\n")

print unicode(parsedPage)
