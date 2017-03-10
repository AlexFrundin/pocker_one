a=5

def f(a):
    b=a
    def g(x):
        return b*x
    def set_b(c):
        nonlocal b
        b=c
    g.set_b=set_b
    return g
double=f(2)
double(2)

double.set_b(3)
double(2)n
