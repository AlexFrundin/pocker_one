def infinity_list():
    i = 0
    while True:
        yield i
        i +=i

for i in infinity_list():
    if i*i >100:
        break
    print(i, i*i)

import itertools
for i in itertools.count(0):
    if i*i >100:
        break
    print(i, i*i)
#ленивые вычисление
list(itertools.takewhile(lambda x: x*x<=100, itertools.count(0)))

def filter_multipliers(p, inf_l):
    for i inf_l:
        if i%p:
            yield i

def get_prime():
    c=itertools.count(2)
    while True:
        prime=next(c)
        c=filter_multipliers(prime,c)
        yield prime

list(itertools.islice(get_prime(),0,10))
    
