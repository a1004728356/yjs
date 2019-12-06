from urllib import request
import json
weather=request.urlopen('http://www.weather.com.cn/data/sk/101100101.html')
aaa=weather.read().decode('utf8')
print(aaa)
print(json.loads(aaa))