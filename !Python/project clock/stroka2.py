s=input("stroka")
st=str()
for char in s:
    if char.isalpha():
        st+=char;
print(st)
for i in range(len(s)):
    if s[i].isalpha():
        st+=s[i]
print(st)
print(s.upper())
