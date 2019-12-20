lista = [1,5,5,6,5,9,8,2,3]
lista.insert(2,'.')
lista.insert(6,'.')
lista.insert(10,'-')
listastr = []
i = 0
while(i <12):
    listastr.append(str(lista(i)))
    i = i+1
listaF = ''.join(listastr)
print(listastr)
print(listaF)