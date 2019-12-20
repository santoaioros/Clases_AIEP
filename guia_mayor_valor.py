valores = []
cant = int(input('Ingrese cunatos numeros ingresar: '))
for i in range(1,(cant+1)):
    valores.append(int(input('Ingrese valor nº' + str(i) + ': ')))

valores.sort()
print('El menor valor ingresado es : {}'.format(valores[0]))