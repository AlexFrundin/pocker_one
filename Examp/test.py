def double(x):
    return 2*x

print(list(map(double,[1,2,3,4,5])))
print([2*x for x in [1,2,3,4,5]])


def odd(x):
    return x%2

print(list(filter(odd, [1,5,7,10])))
