def my():
    data.sort()
    a=len(data)
    if a%2: return data[a//2]
    else: return float((data[a//2-1]+data[a//2])/2)
 
data=[int(x) for x in input().split(' ')]
if(data):
    print(my())