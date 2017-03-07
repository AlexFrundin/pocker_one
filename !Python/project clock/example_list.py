# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:39:20 2015

@author: student
"""

data =input("Введите ваши данные через пробел:")
list1=data.split()#разбивка строки на подстроки для формирования лист
print(list1)
b=[]
for x in list1:
    b.append(int(x))
print(b)
s=0
for x in b:
    s+=x
average=s/len(b)
b.sort()
er=(b[-1]-b[0])/2
print(average, er)