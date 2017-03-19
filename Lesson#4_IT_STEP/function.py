hero={
'strength':53,
'power':67,
'name':'Bobi',
"age":45,
'money':-58,
'items':
{
'milk':2,
'beef':3,
'water':4
},
'weapon':[10,35,-90,'not work']
}




for damage in hero['weapon']:
    try:
        if damage>0:
            print('Damage=', damage)
        elif damage<0:
            print('You hiald enemy  ', damage)
    except:
        print('Bad weapon')
