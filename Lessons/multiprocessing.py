from  multiprocessing import Process

a=0
def f():
    global a
    for i in range(1000):
        a+=1
    print(a)
ps=[]
for i in range(100):
    #p=multiprocessing.Process(target=f)
    p=multiprocessing.Process(target=f)
    p.start()
    ps.append(p)

for p in ps:
    p.join()

print(a)
#IPC
"""
POSIX
1 pipe каналы передачи данных проще в реализации существует два процесса синхронно, использует ядро
2 mq очереди сообщений использует ядро, асинхронная
3 shm не использует ядро, отдельный обьект в памяти, но не обладает возможностью синхроннизации данных без дополнительных оберток
4 socket
Windows

"""
