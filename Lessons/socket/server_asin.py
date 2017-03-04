import select
import socket


def handle(c):
    data=c.recv(1024)
    #must have для закрытия не используемых сокетов
    if not data:
        c.close()
        connections.remove(c)
        return
    print(data)
    c.sendall(data)

s=socket.socket()
s.bind(('localhost',5000))

s.setblocking(False)

s.listen(5)
print('server started')

connections=[s]

while True:
    reading_sockets, _, _=select.select(connections,[],[])
    for socket_ in reading_sockets:
        if socket_==s:
            c,a =s.accept()
            print("connected",a)
            connections.append(c)
        else:
            handle(socket_)
