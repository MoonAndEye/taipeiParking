# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 15:53:40 2016

"""
import urllib.request
import datetime
import json
import pandas as pd
import gzip


file_name = "test.gz"

url = 'http://data.taipei/tcmsv/allavailable'

urllib.request.urlretrieve(url, file_name)
