# try:
#     age = int(input("Сколько тебе лет?\n"))
# except:
#     age=0
# if age>0 and age <=17:
#     print("Подросток")
# elif age<23:
#     print("Студент")
# elif age <110:
#     print("Рабочая лошадь, гы-гы-гы!!!")
# else:
#     print("ВЫ НЕ ЧЕЛОВЕК!!!!!!!!!")

#
# name=int(input("Number"))
#
# if name == 0:
#     print("Hello")
# else:
#     print("Bye")

import time
a=time.localtime()
print(a.tm_year)
