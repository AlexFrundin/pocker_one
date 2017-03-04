import urllib.request
import threading
import queue
#выполняется 8 секунд
'''for i in range (20):
    t=urllib.request.urlopen('http://mail.ru')
    print(len(t.read()))


print(t.read())
'''
q=queue.Queue()
#выполняется быстрее в 2.5 раза
def geturl():
    while True:
        url=q.get()
        t=urllib.request.urlopen('http://mail.ru')
        print(len(t.read()))
        q.task_done()

for i in range(4):
    t=threading.Thread(target=geturl)
    t.daemon=True
    t.start()

for i in range(20):
    q.put('http://mail.ru')

q.join()
