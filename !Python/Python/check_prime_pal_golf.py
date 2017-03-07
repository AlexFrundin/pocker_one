a=int(input())
while 1:
    a+=1
    for i in range(2,data//2):
        if not a%i: break
    else:
        if str(a)==str(a)[::-1]:
            return a
    