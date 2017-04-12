import time
import random

def  coroutine(f):
    def wrapper(n):
        gen=f(n)
        next(gen)
        return gen
    return wrapper

@coroutine
def g(n):
    yield
    while True:
        i = yield n
        print(n)


coros = {5:g(1), 3:g(2)}
sec=0
while True:
    print('1 tic')
    time.sleep(1)
    sec+=1
    for interval in coros:
        if not sec % interval:
            coros[interval].send(random.randint(1,100))
