list_number=[1,5,10,20]
number=50
expansions=[]
temp=[]
def func(temp,list_):
    if len(list_)==0:
        return
    for i in list_:
        temp.append(i)
        if sum(temp)==20:
            expansions.append(temp)
        elif sum(temp)<20:
            func(temp,list_)
        elif sum(temp)>20:
            func(temp[:-2],list_[1:])
        temp=[]
        func(temp,list_[1:])

list_number.reverse()
func(temp,list_number)

for item in expansions:
    item.sort()



for i in expansions:
    print(i)
