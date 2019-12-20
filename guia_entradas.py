entradas = int(input('Ingrese el Nº de entradas vendidas en pre-venta: '))
i = 0
while (i == 0):
    asistentes = int(input('Ingrese el Nº de personas que asistieron al recital: '))
    if(asistentes > entradas):
        print('Error! El numero de asistentes al recital es mayor a la cantidad de entradas')
    else:
        i = 1

if(asistentes < entradas):
    print('Falto que asistieran al recital este numero de personas: ')
    print(entradas - asistentes)
else:
    print('La cantidad de asistentes es la misma a las entradas vendidas')
