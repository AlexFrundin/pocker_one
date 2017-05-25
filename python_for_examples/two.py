def my_input():
    return [input() for _ in range(int(input("quantity->")))]

def my_file():
    name = input('name file->')
    with open(name, 'r') as f:
        for _ in range(2):
            yield [f.readline().strip() for _ in range(int(f.readline()))]

def statistic(one, two):
    for i in range(len(two)):
        n=0
        for item in one:
            if two[i]==item:
                n+=1
        yield n

if __name__=="__main__":
    choice = int(input("1-from console, other - from file->"))
    if choice==1:
        info = my_input()
        test=my_input()
    else:
        gen = my_file()
        info = next(gen)
        test=next(gen)
        
    for item in statistic(info, test):
        print(item)
