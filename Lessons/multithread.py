import threading

def hello(i):
    print('hello{}'.format(i))

for i in range(10):
    t=threading.Thread(target=hello,args=(i,))
    t.start()
