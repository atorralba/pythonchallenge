#!/usr/bin/python

import requests
import re

r = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")

match = re.search("<!--(.|\n)*-->", r.content)

if not match:
	print "match not found"
	exit(1)

text = match.group().replace('<!--','').replace('-->','').replace('\n','')

match = re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", text)

if not match:
	print "match not found"
	exit(1)

print ''.join(match)