def add_x(cls):
    cls.x=1
    return cls

@add_x
class A:
    y=2

print(vars(A))

a=A()

print(a.x)
