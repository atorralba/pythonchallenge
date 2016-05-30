#!/usr/bin/python

import urllib
from PIL import Image
import re

urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "oxygen.png")
img = Image.open("oxygen.png")

box = (0, 43, 608, 52)
cropped_img = img.crop(box)
size = width,height = cropped_img.size
pix = cropped_img.load()

val = 0
text = ''
for x in range(0,width,7):
	color = pix[x,0][0]
	text += chr(color)
	val = color

print text

sol = ''
for n in re.findall(r'\d+',text):
	sol += chr(int(n))

print sol
