#!/usr/bin/python

import sys
import os.path
import xml.etree.ElementTree as xml

def readfile(fh):
	xmltree = xml.parse(fh)
	print "xml: %s" % xml

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

