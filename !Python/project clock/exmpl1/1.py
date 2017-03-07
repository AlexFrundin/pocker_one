# -*- coding: utf-8 -*-
import os
os.system("cls")
name=input("your name: ")
age=int(input("your age: "))
if age<25:
	print("Mister",name, "student")
	print(" Worker", 25-age)
elif age>=25 and age<55:
	print("Mister",name,"is you worker")
	print("pensia ", 55-age)
else:
	print("Вы пенсионер")
os.system("pause")

