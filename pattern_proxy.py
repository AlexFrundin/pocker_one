class A:
    def m1(self):
        print("M1")
    def m2(self):
        print("M2")
    def m3(self):
        print("M3")

class Proxy:
    def __init__(self):
        self.a=A()
    def m1(self):
        print("Proxy.m1")
    def __getattr__(self,name):
        return getattr(self.a, name)

p=Proxy()
p.m1()
p.m2()

class D:
    def f(self):
        print("D.f")

p.a=D()
p.f()
