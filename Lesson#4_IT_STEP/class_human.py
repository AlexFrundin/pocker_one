

class Human():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.life=100
    def __str__(self):
        return ("my name is {} and my age is {} years".format(self.name, self.age))

    def gogo(self,name):
        return (name, 'go')

    def command(self, command_):
        if command_=='go':
            return 'go'
        else:
            return 'no'
