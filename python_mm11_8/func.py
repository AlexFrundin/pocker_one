

import random
level=[]

row=20
col=20


for i in range(row):
    level.append([])
    for j in range(col):
        level[i].append(random.randint(0,2))

for row in level:
    print("")
    for col in row:
        if col==0:
            print(" ", end="")
        elif col ==1:
            print("#",end="")
        else:
            print("|", end="")
#на основе  двумерного массива построить одномерный 
