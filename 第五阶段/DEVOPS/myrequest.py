#'pip3 install requests'
import requests
# payload={'wd':'centos7'}
# r=requests.get('http://www.baidu.com/s',params=payload)
#相当于访问http://www.baidu.com/s?wd=centos7
#################################################
#请求时，加上指定的头部信息
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r=requests.get('http://127.0.0.1',headers=header)
########################################################0
#data用于提交表单数据
# data={'usename':'xxx','password':'yyyyyy'}
# r=requests.post('http://login.baidu.com',data=data)
#######################################
#获得网页信息
r=requests.get('http://www.baidu.com/')
data=r.text#查看页面内容，默认的文字编码是ISO8859-1
r.encoding('utf8')
#######################
r2=requests.get('http://g.hiphotos.baidu.com/exp/w=500/sign=67597f61b951f819f125034aeab54a76/09fa513d269759ee63269981bbfb43166d22df02.jpg')
with open('a.jpg','wb') as fobj:
    fobj.write(r2.content)#content是bytes格式
