from  ModelContact import PhoneBook
from ViewContact import *
from XML_Mode import MakeTree
from DOM_parser import ParserTree_DOM
from Parser_sax import parser_sax
from Parser_STAX import parserStax
import os

class Controller():
    def __init__(self,name):
        self.name=name
        self.__contacts=PhoneBook()
        #if  os.path.exists('{}.xml'.format(name)):
            #self.loadXML()


    def create(self, name, number):
        self.__contacts[name]=number

    def update(self, name, number):
        self.__contacts[name]=number

    def delete(self,name):
        del(self.__contacts[name])

    def __len__(self):
        return len(self.__contacts)

    def save(self):
        pass

    def loadSTAX(self):
        for item in parserStax(self, ('name','number')):
            self.create(*item)

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
#not like
    def __str__(self):
        for name, number in self.get_contact():
            print ("name {}\nnumber {}\n".format(name,number))
        return ""


a=Controller('one')
a.loadSTAX()
print(a)
#a.create('Vasya','067')
#a.create('Vasya1','0671')
#a.create('Vasya2','0672')
#a.saveXML()
#a.loadXML()
#MakeTree(a)
#a.load_task()
#print(a)
