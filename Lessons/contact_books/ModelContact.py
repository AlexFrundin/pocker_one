#для полной инкапсуляции можно передавать каждый объект как класс
#тогда вся логика выйдет в модель где описан класс
#все фуекции в контроллере будут принимать экземпляр класса
#такая модель плохо подходит для реализации в СУБд
#но предполагаю что можно связать каждый ID с чем-то уникальным в классе
#допустим использовать статическую переменную в классе, даже если
#контакт будет изменен, его порядковый номер останется не изменным
#создадим функцию, которая будет возвращать его для СУБд

class PhoneBook():
    def __init__(self):
        self.dict={}

    def __contains__ (self, name):
        return name in self.dict

    def __getitem__(self, name):
        return self.dict[name]

    def __setitem__(self,name,number):
        if name not in self.dict:
            self.dict[name]=number
        else:
            raise KeyError

    def __len__(self):
        return len(self.dict)

    def __iter__(self):
        return iter(self.dict)

    def __delitems__(self,name):
        if name not in self.dict:
            raise KeyError
        else:
            del(self.dict[name])
