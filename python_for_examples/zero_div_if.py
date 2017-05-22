while True:
    a = input("Enter to number->")
    if a.isdigit():
        a=int(a)
        if a==0:
            print('Bad operation')
        else:
            print(100/a)
    else:
        print('bye')
        break
