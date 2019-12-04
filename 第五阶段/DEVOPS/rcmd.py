import paramiko
def rcmd(host,password,cmd,port=22,username='root'):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        username=username,
        password=password,
        port=port
    )
    stdin,stdout,stderr=ssh.exec_command(cmd)
    data=stdout.read().decode('utf8')
    error=stderr.read().decode('utf8')
    if data:
        print('[%s:OUT]:\n%s' % (host,data))
    if error:
        print('[%s:ERROR]:\n%s' % (host, error))
    ssh.close()
if __name__ == '__main__':
    rcmd('192.168.16.63','123456','ls /root')