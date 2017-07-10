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
    group=[]
    with open(name_file, "r") as f:
        for line in f.readlines():
            group.append(Human(*(line.rstrip().split(','))))
    return group

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
        self.age=int(age)
        self.height=int(height)

    def __str__(self):
        return ("name={}\nage={}\nheight={}\n".format(self.name, self.age, self.height))

    def info(self):
        return ("{},{},{}\n".format(self.name, self.age, self.height))




answer=input("вы хотите загрузить из файла? 1- да")

if answer=="1":
    group=load("Group.txt")
else:
    group=create_group()





for item in group:
    if item.age>18:
        print(item)
