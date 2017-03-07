# -*- coding: utf-8 -*-
import random
def displayMatrix(x):
    print()
    for row in x:
        for elem in row:
            print("{:4d}".format(elem),end=" ")
        print()

a=[[0]*5]*5
displayMatrix(a)
rows=9
cols = 9
b=[0]*rows

for i in range(rows):
    b[i]=[0]*cols
    for j in range(cols):
        b[i][j]=random.randint(4,12)

for row in b:
    row.sort()
s=[]
print()
for row in b:
    summ=0
    for mark in row:
        summ+=mark
    aver =summ/cols
    s.append(aver)

displayMatrix(b)

for av in s:
    print ("{:.1f}".format(av))