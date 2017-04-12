import time
import random

def  coroutine(f):
    def wrapper(*n):
        gen=f(*n)
        next(gen)
        return gen
    return wrapper

@coroutine
def g(n,s):
    yield
    while True:
        print('g')
        i = yield from sleep(s)
        print('g',i)


@coroutine
def sleep(s):
    yield
    while True:
        print('s')
        yield s

coros=[g(1,5),g(2,3)]
sec_coros={}



for coro in coros:
    print(coro)
    s=coro.send(None)
    print(s)
    sec_coros[s]=coro

input()
sec=0
while True:
    time.sleep(1)
    sec+=1
    print(sec_coros)
    for i in sec_coros:
        if not i%sec:
            sec_coros[i].send(random.randint(1, 100))
