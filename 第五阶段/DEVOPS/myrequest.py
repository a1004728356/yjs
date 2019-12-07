#'pip3 install requests'
import requests
# payload={'wd':'centos7'}
# r=requests.get('http://www.baidu.com/s',params=payload)
#相当于访问http://www.baidu.com/s?wd=centos7
#################################################
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r=requests.get('http://127.0.0.1',headers=header)