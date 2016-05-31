#!/usr/bin/python

import io
import requests
from requests.auth import HTTPBasicAuth
from PIL import Image

r = requests.get("http://www.pythonchallenge.com/pc/return/cave.jpg",
	auth=HTTPBasicAuth("huge", "file"))

img = Image.open(io.BytesIO(r.content))

width,height = img.size

result = Image.new('RGB', (width,height))

pixels = img.load()
result_pixels = result.load()

for x in range(width):
	for y in range(height):
		pix = pixels[x,y]
		if x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1:
			result_pixels[x,y] = pixels[x,y]

result.show()
