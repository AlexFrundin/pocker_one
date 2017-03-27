import os

def save(group):
    f=open("Group.txt","w")
    for item in group:
        f.write(item.info())
    f.close()


def load(name_file):
    if not os.path.exists(name_file):
        print("No file")
        return
    f=open(name_file, "r")
    temp_group=f.readlines()
    f.close()
    group=[]
    for human in temp_group:
        group.append(human.split(","))
    print(group)



def create_group():
    len_group=int(input("Сколько в группе человек?"))
    group=[]

    for i in range(len_group):
        print ("Введите данные кандита №{}:".format(i+1))
        name=input("Имя->")
        age=int(input("Возвраст->"))
        height=int(input("Рост->"))
        group.append(Human(name,age,height))
        os.system('cls')

    save(group)
    return group

class Human():
    def __init__(self, name, age, height):
        self.name=name
        self.age=age
        self.height=height

    def __str__(self):
        return ("name={}\nage={}\nheight={}\n".format(self.name, self.age, self.height))

    def info(self):
        return ("{},{},{}\n".format(self.name, self.age, self.height))




answer=input("вы хотите загрузить из файла? 1- да")

if answer=="1":
    load("Group.txt")
else:
    group=create_group()





'''for item in group:
    if item.age>18:
        print(item)
'''
