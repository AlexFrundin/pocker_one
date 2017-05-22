while True:
    try:
        one= int(input("Введите первое число->"))
        two=int(input("Введите второе число->"))
    except:
        print("Ты редиска")
        continue
    z = input("Введите знак операции")
    if z=='+':
        print(one+two)
    elif z=='-':
        print(one-two)
    elif z=='*':
        print(one*two)
    elif z=='/':
        if two !=0:
            print(one/two)
        else:
            print("Ты плохой и не умный человек!!!")
    else:
        break
