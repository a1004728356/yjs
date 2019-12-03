#为了防止由于服务器限制，不能通过程序爬取页面，模拟使用firefox浏览
from urllib import request
url='http://139.9.235.209/'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
r=request.Request(url,headers=header)
html=request.urlopen(r)
data=html.read()
print(data.decode('utf8'))
