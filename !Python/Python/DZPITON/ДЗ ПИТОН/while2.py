# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:43:19 2016

@author: 1
"""
import os
a=int(input("Введите натуральное число->"))
if a%a==0 and a%1==0 and a>1 and a%2==1:
    print("ваше число простое")
else :
    print("Введённое число не простое")
os.system("pause")