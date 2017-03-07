text=input()
palindrom =[]
l=len(text)
for i in range(l):
    for j in range(l,i,-1):
        print (text[i:j],text[j::-1],j,i)
        if text[i:j]==text[j::-1] and j-i!=1:
            palindrom.append(text[i:j])
print (palindrom)
