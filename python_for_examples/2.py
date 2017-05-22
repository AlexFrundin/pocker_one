summa=0
while True:
    try:
        summa+=int(input("Введите число->"))
    except:
        print('Bye!!!')
        break
print(summa)
