def my_input():
    info=[]
    for _ in range(int(input())):
        info.append(input())
    return info

info = my_input()
test={item:0 for item in my_input()}

# for i in info:
#     if i in test:
#         test[i]+=1

test.update(test[i], test[i]+1 for i in info if i in test)
print(test)
