defacto = {'Ж':'Г-жа ','М':'Г-н '}

# def test(fn):
#     def wrapp():
#         for item in sorted(fn(), key=lambda x: int(x[-1])):
#                 print (defacto[item[-2]]+' '.join(item[:-2]))
#     return wrapp
def test(fn):
    def wrap():
        return [(defacto[item[-2]]+' '.join(item[:-2])) for item in sorted(fn(), key=lambda x:int(x[-1]))]
    return wrap

@test
def my_input():
    return [input().split() for _ in range(int(input()))]
@test
def my_file():
    name = input("Enter name to file->")
    with open(name, 'r') as f:
        return [f.readline().strip().split() for _ in range(int(f.readline()))]

if __name__=='__main__':
    n = int(input("Enter 1-from console, other digital -from file->"))
    if n==1:
        print('\n'.join(my_input()))
    else:
        print('\n'.join(my_file()))
