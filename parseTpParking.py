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
data = gzip.decompress(data) # data在這一步還是 byte
data = data.decode("big5") #到這一步才能把 byte 轉成 string

#print(data)

text1 = json.loads(data)

result = text1["data"]["park"]

b4csv = pd.DataFrame(result)

b4csv["availablecar"]  = b4csv["availablecar"].astype(int)

b4csv = b4csv[b4csv.availablecar > 0]

b4csv = pd.DataFrame.reset_index(b4csv)

b4csv = b4csv.drop("index", 1)
"""
aftcsv = pd.DataFrame.to_csv(b4csv)

csv_file = open(file_path + str(d0)+'.csv', 'w', encoding = 'utf-8' )

csv_file.write(aftcsv)

csv_file.close()

print ('The ' + str(d0) + ' is done')
"""
