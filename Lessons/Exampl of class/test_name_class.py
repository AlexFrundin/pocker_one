class ReprMixin:
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ','.join(["{}={}".format (k,v) for k,v in self.__dict__.items()]))


class Person(ReprMixin):
    def __init__(self,name,age):
        self.name, self.age=name,age

p=Person('Bi',21)


class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A,B):
    def __init__(self):
        print('C')
        super().__init__()

print(C())
