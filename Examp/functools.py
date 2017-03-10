import functools

def add(x,y):
    return x+y

print(functools.reduce(add,[1,2,3,4,5]))

print(functools.reduce(lambda a,x:a*x,[1,2,3,4,5]))
