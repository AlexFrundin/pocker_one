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
        return "Name: {}, Age: {}, Gender: {}\n level of hungry ={}\n level of Thirst={}".format(self.__name, self.__age,
             'Man' if self.__gender else 'Woman',self.__hunger,self.__thirst)

    def __getAge(self):
        return self.__age

    def __setAge(self, time):
        if time>0:
            self.__age+=time

    def __getHunger(self):
        return self.__hunger

    def Feed(self,value):
        self.__hunger+=value
        if self.__hunger>100:
            self.__hunger=100

    def Drink(self,value):
        self.__thirst+=value
        if self.__thirst>100:
            self.__thirst=100

    def __getThirst(self):
        return self.__thirst

    StreamLife=property(__getAge,__setAge)
    Hungry=property(__getHunger)
    Thirst=property(__getThirst)
