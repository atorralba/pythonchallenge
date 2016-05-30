#!/usr/bin/python

import urllib2
import base64
import re
from PIL import Image, ImageDraw

request = urllib2.Request("http://www.pythonchallenge.com/pc/return/good.html")
base64string = base64.encodestring('%s:%s' % ('huge', 'file')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request).read()

first = [ int(x) for x in re.search(r'first:\n([0-9],?\n?)*', result).group().replace('first:', '').replace('\n', '').strip().split(',') ]
second = [ int(x) for x in re.search(r'second:\n([0-9],?\n?)*', result).group().replace('second:', '').replace('\n', '').strip().split(',') ]
maximum = max(max(first),max(second))

image = Image.new('RGB', (maximum, maximum))
draw = ImageDraw.Draw(image)
for i in range(0, len(first)-3, 2):
	first_px = (first[i], first[i+1])
	second_px = (first[i+2], first[i+3])
	draw.line((first_px,second_px), fill=255)

for i in range(0, len(second)-3, 2):
	first_px = (second[i], second[i+1])
	second_px = (second[i+2], second[i+3])
	draw.line((first_px,second_px), fill=255)

image.show()
