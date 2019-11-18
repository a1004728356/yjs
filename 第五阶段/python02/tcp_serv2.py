import socket

host = ''  # 表示监听在0.0.0.0
port = 12345  # 端口号，应该>1024
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
while True:
    cli_sock, cli_addr = s.accept()
    print('client connected from:', cli_addr)
    while True:
        data=cli_sock.recv(1024)
        if data.strip()==b'quit':
              break
        print(data.decode('utf8'))
        sdata=input('>')
        sdata='%s\r\n' % sdata
        cli_sock.send(sdata.encode('utf8'))
    cli_sock.close()
s.close()

