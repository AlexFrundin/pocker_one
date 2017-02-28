import time

def func(f):
    def decorator(i,beg, end):
        gen=f(i,beg,end)
        next(gen)
        return gen
    return decorator

@func
def setPos(i,beg,end):
    while True:
        while i>=beg  and i<end:
            yield i
            i=i+1
        while i<=end and i>beg:
            yield i
            i=i-1

while True:
    i=setPos.send(1)
    print(i)
    time.sleep(0.5)
