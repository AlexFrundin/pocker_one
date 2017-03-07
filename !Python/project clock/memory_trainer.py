# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:56:32 2015

@author: student
"""
import random
q=0
n =int(input("Введите количество попыток: "))
for k in range(n):
    x=random.randint(1,9)
    y=random.randint(1,9)
    print(x,"x",y,"=",end=" ")
    z=int(input())
    if z==x*y:
        q+=1
mark=12*q/n; print("Ваша оценка:",mark)