
st=('a','b','c','d')
for i in st:
    exec(('{0}=1').format(i))
print(globals())
