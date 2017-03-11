class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return ("The dog is name {}".format(self.name))

    def exec_(self, name, command, obj):
        if name==self.name:
            if command=='go':
                self.go(obj)


    def go(self, obj):
        print('Run to human is name {}'.format(obj.name))

    def exec_2(self, command):
        if command=='go':
            print('Run')
        else:
            print('Gav')
