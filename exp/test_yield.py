import time

def setPos(begin, end):
    i=begin
    while i>=begin and i<end:
        yield i
        i=i+1
    while i<=end and i>begin:
        yield i
        i=i-1



def test():
    for i in setPos(10,20):
        return (i)
        time.sleep(0.5)



def func():
    try:
        func.i+=1
        if func.i>=1 and func.i<10 and func.check:
            return func.i
        elif func.check:
            func.check=False
            return func.i
        else:
            func.i-=2
            if func.i<=1:
                func.check=True
            return func.i
    except AttributeError:
        func.i=0
        func.check=True
        return func.i

def func2():
    if not hasattr(func2,'i'):
        func2.i=0
        func2.check=True
    func2.i+=1
    if func2.i>=1 and func2.i<10 and func2.check:
        return func2.i
    elif func2.check:
        func2.check=False
        return func2.i
    else:
        func2.i-=2
        if func2.i<=1:
            func2.check=True
        return func2.i


while True:
    print(func2())
    time.sleep(0.5)
