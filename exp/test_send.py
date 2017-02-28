import time
def coroutine(f):
    gen=f()
    next (gen)
    return gen

@coroutine
def setPos():
    while True:
        i=0
        while i>0 = and i<10:
            yield i
            i=i+1
        while i<=10 and i>0:
            yield i
            i=i-1





while True:
    i=setPos.send(3)
    print(i)
    time.sleep(0.5)
