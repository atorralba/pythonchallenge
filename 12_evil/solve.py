#!/usr/bin/python

import io
import requests
from requests.auth import HTTPBasicAuth
from PIL import Image

r = requests.get("http://www.pythonchallenge.com/pc/return/evil2.gfx",
	auth=HTTPBasicAuth("huge", "file"))

data = r.content

for i in range(5):
	bytes = data[i::5]
	im = Image.open(io.BytesIO(bytes))
	fi = open('image%s.%s' % (i, im.format.lower()), 'wb')
	fi.write(bytes)
	fi.close()
