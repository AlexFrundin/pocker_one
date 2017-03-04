from ClassTamagochi import Tamagochi
import time
import random
import os

hero=Tamagochi("Sasha", False)

time_=0.1
minusHungry=-4
minusThirst=-20
food=[3,0,0,0,7,12,4]
drinks=[10,20,40]

while hero.StreamLife<=100:
    hero.StreamLife=time_
    hero.Feed(minusHungry)
    hero.Drink(minusThirst)
    print("Перед едой\n",hero)
    if hero.Hungry<0:
        minusThirst=-50
    elif hero.Hungry>0:
        minusThirst=-20
    if hero.Thirst<0:
        print("Game Over, ваш герой прожил {}".format(hero.StreamLife/time_))
        break

    hero.Drink(random.choice(drinks))
    hero.Feed(random.choice(food))
    print("После еды\n",hero)

    time.sleep(0.5)
    os.system('cls')
else:
    print("Victory, он умер от старости)))")
