from collections import defaultdict

info =[['Ivanov', 'paper', "10"],
['Petrov', 'pens' ,'5'],
['Ivanov', 'marker', '3'],
['Ivanov', 'paper', '7'],
['Petrov', 'envelope', '20'],
['Ivanov', 'envelope', '5']]
di = defaultdict(lambda: defaultdict(int))
for i in info:
    c,a,b=i
    di[c][a]+=int(b)

print(len(di))

for client in sorted(di):
    print(client + ':')
    for thing in sorted(di[client]):
        print(thing, di[client][thing])
