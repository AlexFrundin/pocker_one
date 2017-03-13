journal={}

quantity=input("quantity students of group?->")

for i in range(int(quantity)):
    name=input("Name #{}->".format(i+1))
    journal[name]=(input("noets for {}".format(name)))

for key, value in journal.items():
    print ("{}={}".format(key, value))
