# -*- coding: utf-8 -*-
import urllib.request
from city import city

'''
dir(urllib.request)
web = urllib.request.urlopen('http://www.baidu.com')
content = web.read()
f = open('baidu.html', 'w')
f.write(str(content))
f.close()
# print(content)
'''

cityname = input("你想查看哪个城市的天气?\n")
citycode = city.get(cityname)

if citycode:
    url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % citycode
    content = urllib.request.urlopen(url).read()
    print(content)
