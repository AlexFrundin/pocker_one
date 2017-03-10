def f(a,b):
    c = a or b
    print(c)

lst=[1,2,3,4,5,6,7,8]

for i, item in enumerate(lst):
    lst[i]=item*item

class __Foo__():
    pass

class Too(__Foo__):
    pass

b=Too()
