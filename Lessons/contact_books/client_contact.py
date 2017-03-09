import socket

s=socket.socket()
s.connect(('localhost',5000))
while True:
    s.sendall(b"hello")
    data=s.recv(1024)
    print(data.decode('utf-8'))
    choise=input()
    s.sendall(choise)
