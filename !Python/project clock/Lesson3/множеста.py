# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:32:35 2015

@author: student
"""
"""
(set) множества - это неупорядоченный список неповторяющихся элементов
"""
import os
s={10,20,10,20,50}
print (s)
#example 
file1=open("data.txt","r")
names=file1.read()
file1.close()
a = names.split()
b = set(a)
c=list(b)
c.sort()
file2= open("data2.txt","w")
for x in c:
    file2.write(x+"\n")
print(b)
print(c)

os.system("pause")