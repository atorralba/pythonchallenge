#!/usr/bin/python

import urllib
import zipfile
import re
import sys

urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/channel.zip", "channel.zip")
zfile = zipfile.ZipFile('channel.zip')
file = zfile.open('readme.txt')
readme = file.read()
file.close()

number = re.search(r'start from ([0-9]*)', readme).group(1)
while True:
	filename = number + '.txt'
	comment = zfile.getinfo(filename).comment
	sys.stdout.write(comment)

	file = zfile.open(filename)
	contents = file.read()
	file.close()
	match = re.search(r'nothing is ([0-9]*)', contents)
	if match  == None:
		break
	
	number = match.group(1)

zfile.close()