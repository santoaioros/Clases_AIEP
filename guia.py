import os

def terminar(self):
    continuar = input('Desea realizar otro ejercicio? S/N ')
    if (continuar.upper() == 'S'):
        return False
    else:
        return True

def fullName(self):
    name = input('Ingrese nombre: ')
    lastname = input('Ingrese apellido: ')
    print('Su nombre completo es : ' + name + ' ' + lastname)
    return terminar(salir)

def guia_iva(self):
    precio = int (input('Ingrese el precio del producto: '))
    cantidad = int (input('Ingrese la cantidad comprada: '))
    neto = int(precio * cantidad)
    iva = (neto * 19)/100
    total = (neto + iva)
    print('El valor neto del la compra es:  {}'.format(neto))
    print('El valor del iva es           :  {}'.format(iva))
    print('El valor total de la compra es:  {}'.format(total))
    return terminar(salir)

salir = False
opcion = 0
while(salir == False):
    if(opcion < 9):
        print('╔═══════════════════════════╗')
        print('║    Guia de ejercicios     ║')
        print('╚═══════════════════════════╝')
        print('╔═══════════════════════════╗')
        print('║ 1) Nombre + Apellido      ║')
        print('║ 2) Valor IVA              ║')
        print('║ 3) Promedio notas         ║')
        print('║ 4) Valor mayor            ║')
        print('║ 5) Vuelto de compra       ║')
        print('║ 6) Asistentes recital     ║')
        print('║ 7) Mayor de 3 numeros     ║')
        print('║ 8) Descuento por codigo   ║')
        print('║ 9) Salir                  ║')
        print('╚═══════════════════════════╝')
        print('╔═══════════════════════════╗')
        opcion = int(input('║    Elija el ejercicio     ║ '))
        print('╚═══════════════════════════╝')

        if(opcion == 1):
            salir = fullName(salir)
        if(opcion == 2):
            salir = guia_iva(salir)
        if(opcion == 3):
            salir = fullName(salir)
        if(opcion == 4):
            salir = fullName(salir)
        if(opcion == 5):
            salir = fullName(salir)
        if(opcion == 6):
            salir = fullName(salir)
        if(opcion == 7):
            salir = fullName(salir)
        if(opcion == 8):
            salir = fullName(salir)
        if(opcion == 9):
            salir = True
            