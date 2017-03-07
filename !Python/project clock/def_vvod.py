def min_max(a,b):
    if (a>b):
        return(b,a)
    else:
        return(a,b)
a,b=1,1
while(a!=0 and b!=0):
    a=int(input("a="))
    b=int(input("b="))
    min,max=min_max(a,b)
    print ("min=",min,"max=",max)