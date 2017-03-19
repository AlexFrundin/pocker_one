a=5
b=0
#print(a/b)
try:
    print(a/b)
except TypeError:
    print('TYpe Error')
except:
    print('Not division zero')
