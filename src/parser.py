#!/usr/bin/python
#coding: utf-8

import sys
import os.path
import xml.etree.cElementTree as xml

def readfile(fh=None):
	xmltree = xml.parse(fh)

	#print "prefixed entity should work: %s" % xmltree.find("cato:entity")
	# SyntaxError: prefix 'cato' not found in prefix map

	print "prefixed entity should work: %s" % xmltree.getroot().find("{http://namespaces.cato.org/catoxml}entity/")
	print "prefixed entity should work: %s" % xmltree.getroot().findall("{http://namespaces.cato.org/catoxml}entity/")
	print "prefixed entity should work: %s" % xmltree.getroot().find("{http://namespaces.cato.org/catoxml}entity")
	print "prefixed entity should work: %s" % xmltree.getroot().findall("{http://namespaces.cato.org/catoxml}entity")
	#er = xmltree.find("entity-ref")
	print "this should have something: %s" % xmltree.getroot().findall("*/entity")


	print "this should iterate too:"
	for e in xmltree.getroot().iter("entity"):
		print "e: %s" % e

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

