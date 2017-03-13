'''def a():
    print ("Hello world! I'm student!")

def b(name):
    print ("Hello world! I'm student! My name is {}".format(name))


name=['Anna', 'Kolya','Masha']

for item in name:
    b(item)'''


def eval(number):
    if number%2==0:
        return True
    else:
        return False

a=input("Number->")

if eval(int(a)):
    print ("Четное")
else:
    print("Нечетное")
