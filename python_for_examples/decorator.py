#не нравится использования print как вывод инфо, хочу использовать yield
import os
defacto = ['Г-жа ','Г-н ']

def test(fn):
    def wrapp():
        for item in sorted(fn(), key=lambda x: int(x[-1])):
            if item[-2] == 'М':
                print (defacto[1]+' '.join(item[:-2]))
            else:
                print (defacto[0]+' '.join(item[:-2]))
    return wrapp

@test
def my_input():
    info=[]
    for _ in range(int(input())):
        info.append(input().split())
    return info

@test
def my_file():
    name = input("Enter name to file->")
    info=[]
    if os.path.isfile(name):
        with open(name, 'r') as f:
            for _ in range(int(f.readline())):
                info.append(f.readline().split())
        return info

if __name__=='__main__':
    n = int(input("Enter ->"))
    if n==1:
        my_input()
    else:
        my_file()
