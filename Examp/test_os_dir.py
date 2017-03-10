# -*-coding: utf-8-*-

import os

command = os.popen('dir')
rez=command.read()
command.close()
print('Результат программы')
print(rez[3:-2].encode('cp866'))
#print(rez.encode(""))
