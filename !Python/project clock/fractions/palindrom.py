a=int(input())
digit=int(len(str(a)))-1
print (digit)
d=0
b=a
while a:
    c=a%10
    a=a//10
    d=(d+c*(10**digit))
    digit=digit-1
if b==d:
    print(d)
else:
    print("")