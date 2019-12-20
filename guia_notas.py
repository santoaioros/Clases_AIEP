notas = []
cant = int(input('Ingrese la cantidad de notas a promediar: '))
cont = 0
acum = 0
for i in range(1,(cant+1)):
    notas.append(int(input('Ingrese la nota nº' + str(i) + ': ')))
    acum = int(acum + notas[cont])
    cont = cont + 1

promedio = acum/cant

if (promedio > 39):
    print('Aprobado con un : {}'.format(int(promedio)))
else:
    print('Reprobado con un : {}'.format(int(promedio)))