import msvcrt
import time
import os

hungry=0.0 #в пределах от 1 до 10
life=100.0
drought=0.0 #в пределах от 1 до 10

emotion = [
"""
    0   0
      |
    \___/
""",
"""
    0   0
      |
    -___-
""",
"""
    0   0
      |
     ___
    /   \\
"""
]

eat={
"salad":1.0,
"beef":5.0,
"bread":3.0
}
potables={
"milk":1.0,
"juices":2.0,
"water":5.0
}

#вовращаю сколько отнимать очков жизни в зависимости от уровня голода
def Hungry_(hungry):
    if hungry<1:
        return -2.0
    elif hungry<2:
        return -1.0
    elif hungry<3:
        return 0.0
    elif hungry <7:
        return 1.0
    elif hungry <8:
        return 2.0
    elif hungry <10:
        return 3.0
    else:
        return 10.0

#вовращаю сколько отнимать очков жизни в зависимости от уровня жажды
def Drouth_(drought):
    if drought<1:
        return -5.0
    elif drought<2:
        return -4.0
    elif drought<3:
        return -1.0
    elif drought <4:
        return 0.0
    elif drought <6:
        return 2.0
    elif drought <8:
        return 6.0
    elif drought <10:
        return 12.0
    else:
        return 28.00
#
def Life_(life_,hungry_,drought_):
    a=Hungry_(hungry_)
    b=Drouth_(drought_)
    return life-a-b

def Plus(eat_me, my_ch):
    return (eat_me-my_ch)

def Eat(eat_me, my_item):
    print ("выберите из списка продукты")
    for item in my_item:
        print(item, end=' ')
    choise=input()
    if choise in my_item:
        return Plus(eat_me,my_item[choise])

def Screen(life_, hungry_, drought_, emotion_):
    print('Life= ', int(life_))
    print('Hungry= ', int(hungry_))
    print('Potables= ', int(drought_))
    if life>73:
        print(emotion_[0])
    elif life>34:
        print(emotion_[1])
    elif life>0:
        print(emotion_[2])
    else:
        Dead()
    print("Если вы хотите покормить  нажмите 1\nили напоить меня нажмите 2")

def Dead ():
    print("Game Over")
    input()

while True:
        hungry+=0.1
        drought+=0.3
        life=Life_(life,hungry,drought)
        Screen(life, hungry,drought,emotion)
        if msvcrt.kbhit():
            key=ord(msvcrt.getch())
            if key ==49:
                hungry=Eat(hungry,eat)
            elif key==50:
                drought=Eat(drought,potables)
        time.sleep(0.5)
        os.system('cls')
