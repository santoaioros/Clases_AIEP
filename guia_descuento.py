print('╔════════╦═════════════╦═══════════╗')
print('║ CODIGO ║ NOMBRE DPTO ║ DESCUENTO ║')
print('╠════════╬═════════════╬═══════════╣')
print('║   1    ║   DAMA      ║    30%    ║')
print('║   2    ║   VARON     ║    05%    ║')
print('║   3    ║   NIÑO      ║    20%    ║')
print('║   4    ║   ELECTRO   ║    15%    ║')
print('╚════════╩═════════════╩═══════════╝')

codigo = int(input('Ingrese el codigo del departamento: '))
precio_compra = int(input('Ingrese el precio del producto: '))
can_compra = int(input('Ingrese la cantidad del producto: '))
total = int(precio_compra * can_compra)
if(codigo ==1):
    descuento = int(total *30)/100
    total_final =int(total-descuento)
    print('╔═════════════════════════════╗──────────────')
    print('║Nombre Género................║ DAMA')
    print('║Precio Compra................║ {}'.format(precio_compra))
    print('║Cantidad.....................║ {}'.format(can_compra))
    print('║Total........................║ {}'.format(total))
    print('║Descuento 30%................║ {}'.format(int(descuento)))
    print('╠═════════════════════════════╣──────────────')
    print('║Total Final..................║ {}'.format(total_final))
    print('╚═════════════════════════════╝──────────────')
if(codigo ==2):
    descuento = int(total *5)/100
    total_final =int(total-descuento)
    print('╔═════════════════════════════╗──────────────')
    print('║Nombre Género................║ VARON')
    print('║Precio Compra................║ {}'.format(precio_compra))
    print('║Cantidad.....................║ {}'.format(can_compra))
    print('║Total........................║ {}'.format(total))
    print('║Descuento 05%................║ {}'.format(int(descuento)))
    print('╠═════════════════════════════╣──────────────')
    print('║Total Final..................║ {}'.format(total_final))
    print('╚═════════════════════════════╝──────────────')
if(codigo ==3):
    descuento = int(total *20)/100
    total_final =int(total-descuento)
    print('╔═════════════════════════════╗──────────────')
    print('║Nombre Género................║ NIÑO')
    print('║Precio Compra................║ {}'.format(precio_compra))
    print('║Cantidad.....................║ {}'.format(can_compra))
    print('║Total........................║ {}'.format(total))
    print('║Descuento 20%................║ {}'.format(int(descuento)))
    print('╠═════════════════════════════╣──────────────')
    print('║Total Final..................║ {}'.format(total_final))
    print('╚═════════════════════════════╝──────────────')
if(codigo ==4):
    descuento = int(total *15)/100
    total_final =int(total-descuento)
    print('╔═════════════════════════════╗──────────────')
    print('║Nombre Género................║ ELECTRO')
    print('║Precio Compra................║ {}'.format(precio_compra))
    print('║Cantidad.....................║ {}'.format(can_compra))
    print('║Total........................║ {}'.format(total))
    print('║Descuento 15%................║ {}'.format(int(descuento)))
    print('╠═════════════════════════════╣──────────────')
    print('║Total Final..................║ {}'.format(total_final))
    print('╚═════════════════════════════╝──────────────')