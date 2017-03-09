class Meta(type):
    def __init__(cls, name, parents, props):
        if not hasattr(cls, 'register'):
            print ('Base')
            cls.register={}
        else:
            print('Child')
            cls.register[name]=cls

class A(metaclass=Meta):
    pass

A.register

class B(A):
    pass

print(A.register)
print(B.register)

class D(A):
    pass

print(A.register)
print(D.register)
print(A.register)
