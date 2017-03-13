import re

text = """asdasd
dsafhgas
asdhkujdfghaj"""
pit = '/w+'

#print(len(text.split(' '))+len(text.split('\n')))
#print(len(text.split(' ')))

print(re.findall())

word=0
for i in text:
    if i =='\n' or i==' ':
        word+=1
if word or text:
    word+=1

print(word, text)
