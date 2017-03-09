class Meta(type):
#служит для переопределения метакласса добавление свойства
    def __call__(cls,*args, **kwargs):
        self=type.__call__(cls,*args,**kwargs)
        self.x=1
        return  self

class A(metaclass=Meta):
    pass

a=A()

print(a.x)
