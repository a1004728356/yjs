import requests
import json
#获取zabbix版本号
# url = 'http://139.9.235.209:8080/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     'jsonrpc': '2.0',  # jsonrpc协议版本号，固定的
#     'method': 'apiinfo.version',  # 在zabbix手册上查到的，查询zabbix版本号
#     'id': 1,  # 随便写个数字就好
#     'params':{}  # 没有额外参数
# }
# # zabbix要求提交的数据是json格式
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(list(str(r.content,encoding='utf8').split('\n'))[-1])  # zabbix返回的数据都是json格式
############################
#获取admin的令牌
# url = 'http://139.9.235.209:8080/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#      "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# # zabbix要求提交的数据是json格式
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(list(str(r.content,encoding='utf8').split('\n'))[-1])  # zabbix返回的数据都是json格式
###########################
#检索所有的主机
# url = 'http://139.9.235.209:8080/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "filter": {
#             "host": [
#                 "Zabbix server",
#                 "Linux server"
#             ]
#         }
#     },
#     "auth": "bf749c6199e05af962ac202dd3d46b84",
#     "id": 1
# }
# # zabbix要求提交的数据是json格式
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(list(str(r.content,encoding='utf8').split('\n'))[-1])  # zabbix返回的数据都是json格式
#######################################
#获取主机组
# url = 'http://139.9.235.209:8080/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": ["hostid"],
#         "selectGroups": "extend",
#         "filter": {
#             "host": [
#                 "Zabbix server"
#             ]
#         }
#     },
#     "auth": "bf749c6199e05af962ac202dd3d46b84",
#     "id": 1
# }
# # zabbix要求提交的数据是json格式
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(list(str(r.content,encoding='utf8').split('\n'))[-1])  # zabbix返回的数据都是json格式
#####################
#获取模版
# url = 'http://139.9.235.209:8080/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": ["hostid"],
#         "selectParentTemplates": [
#             "templateid",
#             "name"
#         ],
#         "hostids": "10084"
#     },
#     "auth": "bf749c6199e05af962ac202dd3d46b84",
#     "id": 1
# }
# # zabbix要求提交的数据是json格式
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(list(str(r.content,encoding='utf8').split('\n'))[-1])  # zabbix返回的数据都是json格式
#####################
#获取主机组
# url = 'http://139.9.235.209:8080/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#      "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             # "name": [
#             #     "Zabbix servers",
#             #     "Linux servers"
#             # ]
#         }
#     },
#     "auth": "bf749c6199e05af962ac202dd3d46b84",
#     "id": 1
# }
# # zabbix要求提交的数据是json格式
# r = requests.post(url, headers=headers, data=json.dumps(data))
# a=str(r.content,encoding='utf8').split('\n')[-1]
# b=eval(a)
# for item in b['result']:
#     print(item['groupid'],item['name'])
################
#获取模版
url = 'http://139.9.235.209:8080/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        "filter": {
            # "host": [
            #     "Template OS Linux",
            #     "Template OS Windows"
            # ]
        }
    },
    "auth": "bf749c6199e05af962ac202dd3d46b84",
    "id": 1
}
# zabbix要求提交的数据是json格式
r = requests.post(url, headers=headers, data=json.dumps(data))
a=str(r.content,encoding='utf8').split('\n')[-1]
b=eval(a)
# print(b)
for item in b['result']:
    print(item['templateid'],item['name'])
##############################
#创建主机
url = 'http://139.9.235.209:8080/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
     "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "mylinux",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "139.9.235.209",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "1"
            }
        ],
        "templates": [
            {
               "templateid": "10047"
            }
        ],
        "inventory_mode": 0,
    },
    "auth": "53cf65f9c53646c65757ca8aa4834e9d",
    "id": 1
}
# zabbix要求提交的数据是json格式
r = requests.post(url, headers=headers, data=json.dumps(data))
print(list(str(r.content,encoding='utf8').split('\n'))[-1])