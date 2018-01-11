# -*- coding: utf-8 -*-
import urllib.request
from city import city
import json

url1 = 'http://mobile.weather.com.cn/js/citylist.xml'
content1 = urllib.request.urlopen(url1).read()
# provinces = content1.split(',')

print(content1)
