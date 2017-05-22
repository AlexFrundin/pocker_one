
len=11
for i in range(len):
    if i<=len//2:
        for j in range(i):
            print("1", end="")
        for j in range(10-2*i):
            print("*", end="")
        for j in range(i):
            print("1", end="")
    elif i>len//2:
        for j in range(10-i):
            print("1",end="")
        for j in range(2*i-10):
            print("*",end="")
        for j in range(10-i):
            print("1",end="")
    print("")
