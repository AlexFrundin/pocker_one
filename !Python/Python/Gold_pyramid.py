n=int(input())
i=1;
while n>0:
    n-=i
    if(n>=0):
        i+=i
    else:
        i+=n
print (i)