#!/usr/bin/python

import urllib
from PIL import Image

urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "oxygen.png")
img = Image.open("oxygen.png")
pix = img.load()
size = width,height = img.size
for x in range(width):
	for y in range(height):
		print pix[x,y]