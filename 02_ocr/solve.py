#!/usr/bin/python

import requests
import re
from collections import Counter

r = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
text = r.content
match = re.compile("<!--(.|\n)*-->\n*(<!--(.|\n)*-->)").search(text)

if not match:
	print "no match found"
	exit(1)

code = match.group(2).replace('<!--', '').replace('-->', '').replace('\n','').strip()

results = Counter(code)

for c in list(results):
	if results[c] != 1:
		code = code.replace(c,'')

print code
