#!/usr/bin/python

import urllib
import re

response = 'the next nothing is 12345'
while 'nothing' in response:
	number = re.search(r'the next nothing is ([0-9]*)', response).group(1)
	a = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number)
	response = a.read()
	if 'Divide' in response:
		number = int(number) / 2
		response = 'and the next nothing is ' + str(number)

	print response

