# coding: utf-8
class Tamagochi:
    def __init__(self, name, gender):
        self.__name=name
        self.__gender=gender
        self.__age=0
        self.__hunger=100
        self.__thirst=100
        self.__myName=name

    def __str__(self):
        return "Name: {}, Age: {}, Gender: {}".format(self.__name, self.__age,
             'Man' if self.__gender else 'Woman')

    def __getAge(self):
        return self.__age

    def __setAge(self, age):
        if self.__age<age:
            self.__age=age

    def __getHunger(self):
        return self.__hunger

    def Feed(self,value):
        self.__hunger+=value
        if self.__hunger>100:
            self.__hunger=100

    StreamLife=property(__getAge,__setAge)
    Hungry=property(__getHunger)
    Thirst=property()


son=Tamagochi("Anna", False)
print(son.Hungry)
son.Feed(-10)
print(son.Hungry)
