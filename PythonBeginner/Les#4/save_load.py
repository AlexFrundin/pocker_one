#r-read
#w-write
#a-append
#'''-*-coding: utf-8 -*-

"""f=open("test.txt","r")

fail_my=f.read()


f.write("Hello, my first file")
f.close()

f=open("test.txt","a")

f.write(fail_my)

f.close()"""

def read_file(name="test.txt"):
    f=open(name,"r")
    info=f.readlines()
    f.close()
    return info


print(''.join(read_file()))
