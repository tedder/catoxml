#!/usr/bin/python
#coding: utf-8

import sys
import os.path
#import xml.etree.cElementTree as xml
from lxml import etree as xml

def readfile(fh=None):
	xmltree = xml.parse(fh)

	for e in xmltree.getroot().findall(".//{http://namespaces.cato.org/catoxml}entity-ref"):
		#print "e: %s" % e
		#print " '%s' %s" % (' '.join(e.text.split()), e.attrib.get('value'))
		print " %s=%s" % (e.attrib.get('entity-type'), e.attrib.get('value'))

	#print "this dumps elements so we can see what they contain"
	#for e in xmltree.getroot().iter():
		#print "e: %s/%s" % (e.tag, "")

files = []
for arg in sys.argv[1:]:
	print "arg: %s" % arg
	if os.path.isfile(arg):
		files.append(arg)
	else:
		print "argument doesn't appear to be a file: %s" % arg

print files

for file in files:
	fh = open(file)
	print "fh: %s" % fh
	readfile(fh)

