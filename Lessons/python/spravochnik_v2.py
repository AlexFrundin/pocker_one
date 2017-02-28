#coding:utf-8

import os
import pickle



#Модуль
def create_contact(name, telephone):
    if name not in contacts:
        contacts[name] = telephone
        save(contacts)
    else:
        raise KeyError


def update_contact(name, telephone):
    if name in contacts:
        contacts[name] = telephone
        save(contacts)
    else:
        raise ValueError


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save(contacts)
    else:
        raise ValueError

#Контроллер
def get_name():
    show_msg(0)
    return input()


def get_telephone():
    show_msg(1)
    return input()


def count_menu():
    try:
        menu_num = int(input())
    except ValueError:
        show_msg(6)
        return

    if menu_num > 4 or menu_num < 1:
        show_msg(6)
        return

    if menu_num == 1:
        try:
            create_contact(get_name(), get_telephone())
            show_msg(3)
        except KeyError:
            show_msg(2)

    elif menu_num == 2:
        try:
            update_contact(get_name(), get_telephone())
            show_msg(4)
        except ValueError:
            show_msg(2)
    elif menu_num == 3:
        try:
            delete_contact(get_name())
            show_msg(5)
        except ValueError:
            show_msg(2)
    else:
        cls()
        read_contact()

def save(obj):
    with open('contacts.pickle','wb') as f:
        pickle.dump(obj,f)

def load():
    try:
        #f=open('contacts.pickle','rb')
        #contacts=pickle.load(f)
        #f.close()
        with open('contacts.pickle','rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


#Визуализация
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def read_contact():
    for key in contacts:
        print(('Имя: {}, Телефон: {}').format(key, contacts[key]))


def view_menu():
    print(
        """
        ----------------------------
        |  Телефонный справочник   |
        |                          |
        |         Меню:            |
        |                          |
        | 1) Создать контакт       |
        | 2) Обновить контакт      |
        | 3) Удалить контакт       |
        | 4) Показать все контакты |
        ----------------------------
        """)


def show_msg(key):
    """
    --------------------------------------
    | Ключ |           Значение          |
    --------------------------------------
    |  0   | Введите имя                 |
    |  1   | Введите номер телефона      |
    |  2   | Нет контакта с таким именем |
    |  3   | Контакт добавлен            |
    |  4   | Контакт обновлен            |
    |  5   | Контакт удален              |
    |  6   | Введите цифру от 1 до 4     |
    --------------------------------------
    """
    msg = (
    	   'Введите имя: ',
    	   'Введите номер телефона: ',
    	   'Нет контакта с таким именем',
    	   'Контакт добавлен',
    	   'Контакт обновлен',
    	   'Контакт удален',
    	   'Введите цифру от 1 до 4'
        )

    cls()
    print(msg[key])

if __name__ == "__main__":
    contacts=load()
    while True:
        view_menu()
        count_menu()
