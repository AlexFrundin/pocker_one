class Tamagochi:
#эта функция инициализирует наш экзепляр
    def __init__(self, name, gender):
        self.__name=name
        self.__gender=gender
        self.__age=0
        self.__hunger=100
        self.__thirst=100
#функция для красивого вывода информации о нашем экземпляра
    def __str__(self):
        return "Name: {}, Age: {}, Gender: {}".format(self.__name, self.__age,
                'Man' if self.__gender else 'Woman')
#функции для доступа к переменной self.__age
#функция возвращающая наше зачение
    def getAge(self):
        return self.__age
#функция для установки значений возвраста
    def setAge(self, age):
        if self.__age<age:
            self.__age=age
#новый вид переменной, которая возращает значение нашего возвраста и может его менять
#первым передается функция, которая возвращает возраст, а вторым которая принимает значение
    StreamLife=property(getAge,setAge)



son=Tamagochi("Anna", False)
print(son.StreamLife)
son.StreamLife=6
print("________________________________________________")
print(son.StreamLife)
print("________________________________________________")
son.StreamLife=4
print("________________________________________________")
print(son.StreamLife)
