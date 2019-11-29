from urllib import request
def download(url,fname):
    html=request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data=html.read(1024)
            if not data:
                break
            fobj.write(data)
if __name__ == '__main__':
    download('http://www.hao123.com','/tmp/hao123.html')
    download('https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=5a386be466380cd7f213aabfc02dc651/77c6a7efce1b9d1617bc0e35f0deb48f8c54646f.jpg','/tmp/lol.jpg')
