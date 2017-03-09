from  ModelContact import PhoneBook
from ViewContact import *
from XML_Mode import MakeTree


class Controller():
    def __init__(self,name):
        self.name=name
        self.__contacts=PhoneBook()

    def create(self, name, number):
        self.__contacts[name]=number

    def update(self, name, number):
        self.__contacts[name]=number

    def delete(self,name):
        del(self.__contacts[name])

    def save(self):
        pass

    def load(self):
        pass

    #def saveXML(self,obj):
        MakeTree(obj)

    def loadXML(self):
        pass

    def get_contact(self):
        for key in sorted(self.__contacts):
            yield (key, self.__contacts[key])




a=Controller('one')

a.create('Vasya','067')
a.create('Vasya1','0671')
a.create('Vasya2','0672')
MakeTree(a)
