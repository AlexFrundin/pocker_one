class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return "name={}, age={}".format(self.name, self.age)

    def __repr__(self):
        return "Person name={}, age={}".format(self.name, self.age)

    def __eq__(self,other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name=other.name

    def __lt__(self, other):
        return self.age<other.age
#допустим для использования наш класс в качестве ключа для словаря
    def __hash__(self):
        return hash(self.name)

        
