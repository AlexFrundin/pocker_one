from collections import OrderedDict

def my_input():
    return [input() for _ in range(int(input("quantity->")))]

def my_file():
    name = input('name file->')
    with open(name, 'r') as f:
        yield [f.readline().strip() for _ in range(int(f.readline()))]
        yield [f.readline().strip() for _ in range(int(f.readline()))]

def analitic(one, two):
    for item in two:
        
        two[item]+=1

if __name__=="__main__":
    gen = my_file()
    info = next(gen)
    test=OrderedDict({item:0 for item in next(gen)})

    analitic(info,test)

    print(test)
