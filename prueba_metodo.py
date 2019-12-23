rut = input('ingrese rut: ')
lista = [int(i) for i in rut if i.isdigit()] 
print(lista)
lista.insert(2,'.')
lista.insert(6,'.')
lista.insert(10,'-')
print(lista)
i=0
listaStr =[]
while(i<12):
    listaStr.append(str(lista[i]))
    i=i+1
listaFinal =''.join(listaStr)
print(listaFinal)
