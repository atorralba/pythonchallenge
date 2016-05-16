#!/usr/bin/python

import urllib2
import base64
import re

request = urllib2.Request("http://www.pythonchallenge.com/pc/return/good.html")
base64string = base64.encodestring('%s:%s' % ('huge', 'file')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request).read()

first = [ int(x) for x in re.search(r'first:\n([0-9],?\n?)*', result).group().replace('first:', '').replace('\n', '').strip().split(',') ]
second = [ int(x) for x in re.search(r'second:\n([0-9],?\n?)*', result).group().replace('second:', '').replace('\n', '').strip().split(',') ]
print first + second
