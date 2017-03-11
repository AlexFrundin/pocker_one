from class_human import Human
from Class_dog import Dog

man=Human('Bill',18)
boxer=Dog('Chack',4)


#command=man.gogo('Chack')

'''if command[0]=='Chack':
    boxer.exec_(*command,man)'''

#boxer.exec_(*(man.gogo('Chack')),man)

boxer.exec_2(man.command('run'))
