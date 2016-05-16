#!/usr/bin/python

import urllib
import re

contents = urllib.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").read()

un = re.search('un: \'(.*)\'', contents).group(1)
pw = re.search('pw: \'(.*)\'', contents).group(1)

print un.decode('string_escape').decode('bz2')
print pw.decode('string_escape').decode('bz2')
