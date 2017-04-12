a=input("Mumber one->")
b=input("Number two->")
try:
    c=int(a)/int(b)
    print(c)
except ZeroDivisionError:
    print("You bad-bad-bad!!!!")
except ValueError:
    print("You very bad-bad-bad!!!!")
