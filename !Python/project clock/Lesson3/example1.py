# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:58:01 2015

@author: student
"""

#ГЕНЕРАТОР СПИСКА
import os
import random

a = [k for k in range(10)]
print (a)
b = [15 for k in range(10)]
print (b)
c=[k**3 for k in range(10)]
print (c)

d=[random.randint(1,9) for k in range(30)]#заполнение случайными числами 
print (d)
d.sort()
print(d)
os.system("pause")