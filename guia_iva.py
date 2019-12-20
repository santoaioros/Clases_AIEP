def guia_iva(self):
    precio = int (input('Ingrese el precio del producto: '))
    cantidad = int (input('Ingrese la cantidad comprada: '))
    neto = int(precio * cantidad)
    iva = (neto * 19)/100
    total = (neto + iva)
    print('El valor neto del la compra es:  {}'.format(neto))
    print('El valor del iva es           :  {}'.format(iva))
    print('El valor total de la compra es:  {}'.format(total))
