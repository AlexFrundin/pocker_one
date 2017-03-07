# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:07:05 2016

@author: 1
"""
import os
a=0
b= int(input("Введите число->"))
while b!=0:
    if b>20 :
        a=b+a
        b=int(input("Введите число->"))
    elif b==0 :
        a=a+b
    else :  
        b=int(input("Введите число->")) 
        a=a+b
if a>100:
    print("сумма тех из них, которые больше 20, превышает 100")
elif a==0 :
    print("Ваше число ровняется->",a)
elif a<100:
    print("сумма тех из них, которые больше 20, непревышает 100")
elif a==100 :
    print("сумма тех из них, которые больше 20, ровнa 100")
else :
    print("Вы допустили ошибку")
os.system("pause")