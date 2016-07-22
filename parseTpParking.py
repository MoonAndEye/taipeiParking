# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 15:53:40 2016

"""
import urllib.request
import datetime
import json
import pandas as pd
import gzip, zlib


file_name = "test.gz"

url = 'http://data.taipei/tcmsv/allavailable'

#urllib.request.urlretrieve(url, file_name)
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
data = gzip.decompress(data)

"""
with open(data, "r") as f:
    text = f.read()
    text = text.decode('utf-8')
"""

print(data)
