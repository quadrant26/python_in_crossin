# -*- coding: utf-8 -*-
import urllib.request
from city import city
import json

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
    try:
        url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % citycode
        content = urllib.request.urlopen(url).read()
        data = json.loads(content)
        print(data)

        result = data['weatherinfo']
        str_temp = ('%s \n %s ~ %s') % ( result['weather'], result['temp1'], result['temp2'])
        print(str_temp)
    except:
        print("查询失败")
else:
    print('没有找到该城市')
