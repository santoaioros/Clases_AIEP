venta = int(input('Ingrese el monto de la venta: '))
i = 0
while(i==0):
    pago = int(input('Ingrese el monto del pago: '))
    if(pago < venta):
        print('Error! Dinero insuficiente')
    else:
        i = 1

vuelto = (pago - venta)
if (vuelto > 0):
    print('El vuelto es: ')
    print(vuelto)
else:
    print('No hay vuelto')
