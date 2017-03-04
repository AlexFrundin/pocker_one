def coroutine(f):
    gen = f()
    next(gen)
    return gen


@coroutine
def f():
    print('f start')
    i=yield
    print('f:',i)
    i=yield i+1
    print('f:',i)
    i=yield i+1
    print('f:',i)

def main():
    print('main start')
    i = f.send(1)
    print("main:", i)
    i=f.send(i+1)
    print("main",i)
print('_________')
main()
