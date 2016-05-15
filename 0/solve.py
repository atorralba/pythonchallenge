#!/usr/bin/python

import requests
import re

number = 2**38
r = requests.get("http://www.pythonchallenge.com/pc/def/"+ str(number) +".html")

print re.search(r"URL\=(.*)>",r.content).group(1).replace('"', '')