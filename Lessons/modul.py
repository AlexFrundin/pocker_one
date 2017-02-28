#модуль создает пространство имен
#как сделать reload модуляё

print("Module 1")

a=5
#modul.a.__maodule__ -показывает к какому модулю она относится
def f():
    print(a)


print(__name__)

if __name__=='__main__':
    print('Start')
