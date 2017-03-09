class A(object):
    x=1

B=type("B", (object,), {'x':1})

class Meta(type):
    def __new__(cls, name, parents, props):
        new_props={}
        for name, value in props.items():
            if not name.startswith('unused_'):
                new_props[name]=value
        return super().__new__(cls,name, parents, new_props)

class C(metaclass=Meta):
    a=1
    unused_b=a

class D(C):
    b=2
    unused_b=2

print(vars(D))
