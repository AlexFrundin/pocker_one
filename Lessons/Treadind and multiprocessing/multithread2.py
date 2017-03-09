import threading

a=0

def f():
    global a
    for i in range(10000):
        a+=1
ts=[]
for i in range(100):
    t=threading.Thread(target=f)
    t.start()
    #ts.append(t)

#for t in ts:
    #t.join()

print(a)
