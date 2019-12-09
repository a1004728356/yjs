import requests
import json

url = 'http://139.9.235.209:8080/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    'jsonrpc': '2.0',  # jsonrpc协议版本号，固定的
    'method': 'apiinfo.version',  # 在zabbix手册上查到的，查询zabbix版本号
    'id': 1,  # 随便写个数字就好
    'params':{}  # 没有额外参数
}
# zabbix要求提交的数据是json格式
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # zabbix返回的数据都是json格式