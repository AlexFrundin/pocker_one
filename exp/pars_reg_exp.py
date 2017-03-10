import re


lst_=r'<name>Vasya Tanja Lina 123</name>'


reg=r'>[\w+ ]+<'



str_=''.join(re.findall(reg,lst_))[1:-1]
print (str_)
'''

dict_rus={'button1':"стоп"}
dict_eng={'button1':"stop"}


def f(choise):
    if choise==1:
        slang=dict_rus
    else:
        slang=dict_eng
    for i in slang:
        print(slang[i])
f(1)
print("------------------------------------")
f(0)
'''
