# import random
#
# mas=[]
#
# for i in range(10):
#     mas.append(random.randint(1,100))
#
# for elem in mas:
#     print(mas)

while True:
    a=int(input("Enter->"))
    s=0
    while a>0:
        s+=a%10
        a=a//10
    print(s)
