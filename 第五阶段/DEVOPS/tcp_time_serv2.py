import socket
from time import strftime
import os
class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def handle_child(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = data.decode('utf8')
            sdata = '[%s] %s' % (strftime('%H:%M:%S'), data)
            cli_sock.send(sdata.encode('utf8'))
        cli_sock.close()

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            pid=os.fork()#创建子进程
            if pid:
                cli_sock.close()#父进程只响应客户端，不用喝客户机通信
            else:
                self.serv.close()#子进程只负责与客户通信，不负责建立连接
                self.handle_child(cli_sock)
                exit()#子进程通信结束后，要退出，不要再进入循环
        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()
