expans=[]

def func(temp,lst):
    temp=[]
    for i in lst:
        temp.append(i)
    expans.append(temp)
    if len(lst)==0:
        return
    func(temp,lst[:-1])

temp=[]
lst=[1,2,3,4,5,6]

func(temp,lst)

print(expans)
expans.reverse()
print(expans)
