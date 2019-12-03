from urllib import request,error
try:
    html=request.urlopen('http://127.0.0.1/xyz/')#xyz不存在
except error.HTTPError as e:#把错误信息保存到e中
    print(e)
try:
    html=request.urlopen('http://127.0.0.1/ban/')#ban无权限访问
except error.HTTPError as e:
    print(e)