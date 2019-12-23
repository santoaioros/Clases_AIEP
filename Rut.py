def validateRut (rut):
    dv = rut[len(rut)-1]
    numbers_list = [int(i) for i in rut[:-1] if i.isdigit()]
    m = 2
    result = 0
    for i in numbers_list[::-1]:
        result = result + (m * i)
        m = m + 1
        if (m ==8):
            m = 2
    dv_calculated = (11 - (result % 11))
    if (dv_calculated == 11 and dv == '0'):
        return True
    if (dv_calculated == 10 and dv.upper() == 'K'):
        return True
    if (dv.isdigit() and dv_calculated == int(dv)):
        return True
    else:
        return False
salir = 0
while(salir==0):
    rut = input('Ingrese el rut: ')
    listaRut = [int(i) for i in rut if i.isdigit()]
    dv = rut[len(rut)-1]
    if (dv.upper() == 'K'):
        listaRut.append('K')
    if (len(listaRut) == 8):
        listaRut.insert(0,'0')
    listaRut.insert(2,'.')
    listaRut.insert(6,'.')
    listaRut.insert(10,'-')
    i = 0
    rutStr = []
    while(i < 12):
        rutStr.append(str(listaRut[i]))
        i = i+1
    rutFinal =''.join(rutStr)
    if (validateRut(rut) == True):
        print('El rut ingresado {} es Correcto'.format(rutFinal))
        salir = 1
    else:
        print('El rut ingresado {} es Incorrecto, intentelo nuevamente'.format(rutFinal))
