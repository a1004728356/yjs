import subprocess
import threading
class Ping:
    # def __init__(self,host):
    #     self.host=host
    def __call__(self,host):
        result=subprocess.call(
            'ping -c2 %s &> /dev/null' % host,
            shell=True
        )
        if result == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)
if __name__ == '__main__':
    ips=['139.9.235.%s' % i for i in range(1,255)]
    for ip in ips:#主线程用于产生工作线程，主线程不会等待工作线程结束
        t=threading.Thread(target=Ping(),args=(ip,))
        t.start()#Ping(ip)()<==>target()mtping2.py
