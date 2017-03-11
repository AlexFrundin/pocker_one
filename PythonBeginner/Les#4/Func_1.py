

def f(beg=None,end=1,value=2):
    if beg==None:
        beg=int(input("Enter first value"))
        end=int(input("Enter second value"))
        value=int(input("Enter value for sort"))
    if beg>end:
        beg,end=end,beg
    item=[]
    for i in range(beg,end+1):
        if i%value==0:
            item.append(i)
    return item

def sort(list_f,value2):
    item=[]
    for i in list_f:
        if i%value2==0:
            item.append(i)
    return item


lst_1=[
[1,100,4],
[20,60,3],
[-86,20,7]
]

for item in lst_1:
    print("item = {}".format(item))
    print(f(*item))
