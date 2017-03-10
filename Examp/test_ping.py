import os

response=os.system('ping 192.168.1.1')

if response==0:
    print('yea')
else:
    print('no')
