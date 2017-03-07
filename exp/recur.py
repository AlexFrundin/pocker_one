

def f(n):
    if n==1:
        return 6
    else:
        return (0.5*f(n-1)+4)


def f_two(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

for i in range(1,10):
    sum_=f_two(i)
    print(sum_)
