# -*- coding: utf-8 -*-

g1 =["vasa","peta","kola"]
g2= ["john","bill","tomy"]
g3 = ["Kaiu","Laon","Naop"]

team=[g1,g2,g3]
print(team)
print("\n")

for group in team:
    for name in group:
        print(name,end=" ")
    print()
print("\n")

for group in team:
    print(group)
print("\n")


for i in range(len(team)):
   for g in i:
       print()