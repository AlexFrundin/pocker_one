#-*-coding: utf-8-*-
import os
contacts={}

def create(name, telephone):
    if name not in contacts:
        contacts[name]=telephone
    else:
        raise ValueError


def delete(name):
    if name in contacts:
        del contacts[name]
    else:
        raise KeyError

def read():
    for item in contacts:
        print (("Имя:{} телефон:{}").format(item, contacts[item]))

def update(name, telephone):
    if name in contacts:
        contacts[name]=telephone
    else:
        raise ValueError

def name_():
    return input('Enter name')

def telephone_():
    return input('Enter telephone')


def view():
    print(
    """
    Для работы с телефонной книгой выберите необходимое действие:
    1-создать
    2-удалить
    3-изменить
    4-вывести телефонную книгу
    """
    )
def val():
    return input("Введите ваш выбор")

def controller(a):
    if a=='1':
        try:
            create(name_(),telephone_())
        except ValueError:
            print ("Такое имя уже есть в книге")
    elif a=='2':
        try:
            delete(name_())
        except KeyError:
            print("Имени нет в списке")
    elif a=='3':
        try:
            update(name (),telephone_())
        except ValueError:
            print("Такого имени нет в списке")
    elif a=='4':
            read()
    else:
        print("Повторите выбор")

def main():
    view()
    controller(val())

while True:
    main()
    os.system('cls')
