class A:
    #создание атрибута readonly (self.a func __setattr__ and __delattr__)
    def __init__(self):
        self.a=42
        #self.f=lambda x:42

    def __getstate__(self):
        print('Get state')
        d= self.__dict__.copy()
#так как функции не серелиазуются мы ее удаляем из словаря
        del d['f']
        return d
    def __setstate__(self,d):
        print('set state')
        self.a=d
        self.f=lambda x:42

#for readonly of self.a
    def __setattr__(self,name, value):
        print('Set attr')
        if name == 'a' and hasattr(self, 'a'):
            raise AttributeError
        super().__init__(name,value)

    def __delattr__(self,name):
        print("Del attr")
        if name=='a':
            raise AttributeError
        super().__delattr__(name)

    def __getattribute__(self,name):
        print("Get Attr")
        return super().__getattribute__(name)
#переопределение для несуществующего аттрибута класса
    def __getattr__(self,name):
        return 42


p=A()
