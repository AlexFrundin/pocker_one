while True:
    try:
        a=int(input("Enter first number->"))
    except:
        continue
    try:
        b=int(input("Enter second number->"))
    except:
        continue
    z=input("Enter operation + - / * -> ")
    if z=="+":
        print(a+b)
    elif z=="-":
        print(a-b)
    elif z=="*":
        print(a*b)
    elif z=="/":
        if b==0:
            print("You bad-human!!!!")
        else:
            print(a/b)
    else:
        print("You bad-human!!!!")
print("Good Bye")
