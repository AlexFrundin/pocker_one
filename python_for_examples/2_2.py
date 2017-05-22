summa = 0
while True:
    a=input("Введите число->")
    if a.isdigit():
        summa=summa+int(a)
    else:
        break
print(summa)
