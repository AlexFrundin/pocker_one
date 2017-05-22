import random
mas=[]
n=10
for i in range(n):
    value=random.randint(1, 100)
    mas.append([value,i])

print("mas= ",mas)

mas.sort(lambda x: x[1],reverse=True)

print(mas)
