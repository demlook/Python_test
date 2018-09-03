#3-4
name=['zjx','hsr','zyl','zj']
absence_guest = 'zj'
print(absence_guest.upper() +' can\'t come on time')
#3-5 add new guest
name.remove(absence_guest)
name.append('lyy')
print(name)
#3-6
print('i find a bigger desk')
name.insert(0,'lpk')
print(name)
name.insert(len(name)//2,'wx')
print(name)
name.append('ws')
print(name)
print("welcome to my party!")
#3-7
print('sorry,i can only invite two persons')
while len(name) != 2:
    name_pop = name.pop().upper()
    print('sorry,goodbye my darlin '+name_pop)
print(name)

