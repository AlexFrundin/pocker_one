import socket
import time
import threading

s=socket.socket()
s.bind(('localhost',5000))
s.listen(5)
#можно подключаться по telnetu
def handle(c):
    while True:
        data=c.recv(1024)
        #must have для закрытия не используемых сокетов
        if not data:
            c.close()
            print("server stop")
            break
        print(data.decode("utf-8"))

print('server started')
while True:
    c,a =s.accept()
    print("connected",a)
    t=threading.Thread(target = handle, args=(c,))
    t.start()



'''c,a=s.accept()
if a:
    data=c.recv(512)
    if data.decode('utf-8').startswith("show"):
        ip_=a[0]
        c.close()
s.close()
return ip_'''
