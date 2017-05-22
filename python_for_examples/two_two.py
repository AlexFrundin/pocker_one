def console_input():
    return [input().split() for _ in range(int(input()))]

def file_input():
    name = input("Name file: ")
    with open(name,'r') as f:
        return [f.readline().strip().split() for _ in range(int(f.readline()))]

print(file_input())
