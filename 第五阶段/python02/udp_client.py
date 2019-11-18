import socket
host='127.0.0.1'
port=12345
addr=(host,port)
c=socket.socket(type=socket.SOCK_DGRAM)
while True:
    data=input('>')
    if data.strip()=='quit':
        break
    sdata='%s\r\n' % data
    c.sendto(sdata.encode('utf8'),addr)
    rdata=c.recvfrom(1024)[0]
    print(rdata.decode('utf8'))