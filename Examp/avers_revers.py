import random


def flyp():
    i=random.randint(1,6)
    if i==1:
        return True
    else:
        return False

def totalFlyp(value):
    sum_heads=0
    sum_tails=0
    for _ in range(value):
        if flyp():
            sum_heads+=1
        else:
            sum_tails+=1

    print("Количество бросков = {}\nОрел выпал {}раз\nРещка выпала {}раз".format(value,sum_heads,sum_tails))


for i in range(10):
    totalFlyp(i)
