# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:13:04 2015

@author: student
"""
import os
#кортеж - неизменяемый список tuple

t=(10,20,30,40,50)#кортеж создается через круглые скобки
a=[10,20,30,40,50]
# t[2]=777
print(t)
print(a)
#задачка про дни недели
days = ("monday","вторни","среда",\
    "чт","пт","суббота","воскресенье")
while True:
    try:#обработка исключений
        n =int(input("Enter number day week:"))
        print(days[n-1])
    except:#
        print("Oops, error:")
    ans = input ("Continued Y/N:")
    if ans=='n':
        break
os.system("pause")