import socket
import time
import threading

s=socket.socket()
s.bind(('192.168.0.200',5000))
s.listen(5)
#можно подключаться по telnetu
def handle(c):
    while True:
        data=c.recv(1024)
        #must have для закрытия не используемых сокетов
        if not data:
            c.close()
            break
        print(data)
        c.sendall(data)

print('server started')
while True:
    c,a =s.accept()
    print("connected",a)
    t=threading.Thread(target = handle, args=(c,))
    t.start()
