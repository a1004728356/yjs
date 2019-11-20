import subprocess
import os
def ping(host):
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
    for ip in ips:
        pid=os.fork()
        if not pid:
            ping(ip)
            exit()