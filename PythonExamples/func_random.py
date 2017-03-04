import time
import os
import random
name=""
age=0
golod=0
jajda=0
plusGolod=3
plusJajda=10
food=[-10,-3,-1,-7,-5,0,5,0]
drink=[-1,-10,-30,-15]

def setName(name_):
    return name_

def status():
    return "{}, {:.2f} лет\n голод={}\n жажда={} ".format(name,age,golod,jajda)

def statusGolod(golod,food):
    golod+=random.choice(food)
    if golod<0:
        golod=0
    return golod

def statusJajda(jajda,drink):
    jajda+=random.choice(drink)
    if jajda<0:
        jajda=0
    return jajda


name=setName(input("Введите имя"))

while age<100:
    age+=0.1
    golod+=plusGolod
    jajda+=plusJajda
    golod=statusGolod(golod,food)
    jajda=statusJajda(jajda,drink)
    print(status())
    if golod>=100:
        plusJajda=40
    elif golod<100:
        plusJajda=10
    if jajda>=100:
        print("Game over")
        break


    time.sleep(0.1)
    os.system("cls")
else:
    print("Умер от старости")
