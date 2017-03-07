s=input()
st=str()
j=0
k=len(s)
while j<k:
    if s[j].isalnum():
        if s[j-1]=='-' and s[j-2].isalpha() and j>2:
            st+=s[j]
            j+=1
        elif s[j].istitle()==0:
            st+=s[j].upper()
            j+=1
        else:
            st+=s[j].lower()
            j+=1
        while (j<k and s[j].isalnum()):
            st+=s[j]
            j+=1
        if not (not (j < k) or not (s[j] in ("?!.,")) or not (s[j + 1] != ' ')):
                st+=s[j]
                st+=' '
                j+=1
    else:
        st+=s[j]
        j+=1
print(st)