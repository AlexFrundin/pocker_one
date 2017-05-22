
while True:
    try:
        one = int(input("Введите первое число->"))
        two = int(input("Введите второе число->"))
    except:
        print("Повтори ввод данных, плохой человек!!!!")
        continue
    z=input("Введите знак операции->")

    if z=='+':
        print(one+two)
    elif z=='-':
        print(one-two)
    elif z=='*':
        print(one*two)
    elif z=='/':
        if two!=0:
            print(one/two)
        else:
            print("Ты очень плохой человек!!!")
    elif z=='s':
        break
    else:
        print("Редиска!!!!")
