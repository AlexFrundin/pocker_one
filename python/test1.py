
temp=[]
def gen(n, lst):
    m=int()
    if n==0:
        temp.append(lst)
    else:
        if len(lst)>0:
            m=min(lst[-1], n)
        else:
            m=n
    for i in range (m, 0,-1):
        gen(n-i, lst+[i])

tmp=[]
gen(5, tmp)
print(temp)
