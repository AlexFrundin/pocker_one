while True:
    try:
        a=int(input("Enter to number->"))
        print(100/a)
    except ZeroDivisionError:
        print("Bad operation!!!")
    except ValueError:
        print('Bye')
        break
