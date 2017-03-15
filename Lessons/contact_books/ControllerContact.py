from  ModelContact import PhoneBook
from ViewContact import *
from XML_Mode import MakeTree
from DOM_parser import ParserTree_DOM
from Parser_sax import parser_sax
from Parser_STAX import parserStax
import os
from contact_DB import create_DB,loadToDB,printDB,update_DB, loadContact
import logging


class Controller():
    def __init__(self,name):
        self.name=name
        self.__contacts=PhoneBook()
        if  not os.path.exists('{}.sqlite'.format(self.name)):
            create_DB(self)
        else:
            print('init')
            self.loadFromDB()
        #self.log=logging
        #self.log.basicConfig(level=logging.DEBUG, filename='{}.log'.format(self.name))
        #if  os.path.exists('{}.xml'.format(name)):
            #self.loadXML()

#использую при включение книги, загружаю всю инфу из бд в телефонную книгу,
#для избежания дублирования записей в бд, так как стандртая create не проверяет
#при добавлении есть ли уже эта инфа в бд(рекурсивное добавления -считывая инфо из бдб она ее же и добавлет)
    def createLoadFromDB(self,name,number):
        self.__contacts[name]=number
#загрузка из бд
    def loadFromDB(self):
        for item in loadContact(self):
            self.createLoadFromDB(*item)

#для создания
    def create(self, name, number):
        try:
            self.__contacts[name]=number
            #update_DB(self,name,number)
        except KeyError:
            self.error_input("create")
        else:
            update_DB(self,name,number)

#при изменении контакта будет происходить дублирование информации в бд,
#надо добавить функцию и в бд
#может лучше удалять базу и снова записывать при закрытии программы
    def update(self, name, number):
        try:
            self.__contacts[name]=number
            #update_DB(self,name,number)
        except KeyError:
            self.error_input("create")
        else:
            update_DB(self,name,number)


    def delete(self,name):
        try:
            del(self.__contacts[name])
        except KeyError:
            self.error_input("create")

    def __len__(self):
        return len(self.__contacts)

    def save_DB(self):
        loadToDB(self)

    def loadSTAX(self):
        for item in parserStax(self, ('name','number')):
            self.create(*item)
#не могу вернуть с класса объект, необходимо в классе парсера использовать методы объекта,not like
    def loadSAX(self):
        print(parser_sax(self))

    def saveXML(self):
        MakeTree(self)

    def loadDOM(self):
        for item in ParserTree_DOM(self):
            self.create(*item)

    def get_contact(self):
        for key in sorted(self.__contacts):
            yield (key, self.__contacts[key])

    def __str__(self):
        contact=[]
        for name, number in self.get_contact():
            contact.append("name {}\nnumber {}\n".format(name,number))
        return "".join(contact)

    def error_input(self,data):
        print("Error")


a=Controller('one')
print(a)


a.create('Vasya1','0671')
a.create('Vasya2','0672')
#a.saveXML()
#a.loadXML()
#MakeTree(a)
#a.load_task()
printDB(a)
