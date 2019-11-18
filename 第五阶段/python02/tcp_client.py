import socket
host='132.232.56.166'
port=12345
addr=(host,port)
c=socket.socket()
c.connect(addr)
while True:
    data=input('>')
    sdata='%s\r\n' % data
    c.send(sdata.encode('utf8'))
    if data.strip()=='quit':
        break
    rdata=c.recv(1024)
    print(rdata.decode('utf8'))
c.close()