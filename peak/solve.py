#!/usr/bin/python

import urllib
import pickle
import sys

urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/banner.p", "banner.p")
file = open('banner.p', 'r')
matrix = pickle.load(file)
file.close()
for x in matrix:
	for y in x:
		sys.stdout.write(y[0] * y[1])
	sys.stdout.write("\n")