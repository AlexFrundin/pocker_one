import random
import time

print("start")
# while True:
#     i=random.randint(0,2)
#     if i ==0:
#         i=' '
#     elif i==1:
#         i='*'
#     else:
#         i='-'
#     j=0
#     while j<90:
#         j=j+1
#     print(i, end='')
summa=0
print("Игра!!! набери 23 очка!")
score=0
while True:
    dice= random.randint(1,6)
    score=score+dice
    print("Выпало {}, у вас сейчас {} очков".format(dice,score))
    print("""
    1 - если продолжить
    2- если начать заново
    3 - если завершить игру
    """)
    try:
        choise = int(input())
    except:
        print("Для вас игра окончена!!!!")
        break
    if choise==1:
        continue
    elif choise==2:
        score=0
    elif choise==3:
        break
    else:
        print("Вы сами виноваты, я продолжаю игру!!!!")
    if score>23:
        print("Вы проиграли")
        score=0
        print("Я думаю, вы хотите отыграться")
