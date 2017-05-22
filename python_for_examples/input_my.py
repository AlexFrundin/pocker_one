q_chet=0
q_nechet=0
s_chet=0
s_nechet=0
while True:
    a=input("Enter number ->")
    if a.isdigit():
        a=int(a)
        if a%2==0:
            q_chet+=1
            s_chet+=a
        else:
            q_nechet+=1
            s_nechet+=a
    else:
        break
print("Summa even of numbers {} and quantity ={}".format(s_chet,q_chet))
print("Summa add of numbers {} and quantity ={}".format(s_nechet,q_nechet))
