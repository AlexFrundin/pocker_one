def f(*args,**kwargs):
    print(args,kwargs)

f(1,2,3, a=1,b=2,z=3)

def f_(a,l=[]):
    l.append(a)
    print(l)


l=[[1,2,3],[4,5,6]]
print(list(zip(l[0],[1])))
print(list(zip(*l)))
