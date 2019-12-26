def validateRut (rut):#definicion de metodo
    dv = rut[len(rut)-1]#variable donde se guarda el digito verificador
    numbers_list = [int(i) for i in rut[:-1] if i.isdigit()]#solo los numeros ingresados sin el digito verificador
    m = 2#variable contadora para la formula del rut validador
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
salir = 0#si cambia a 1 sale del ciclo while
while(salir==0):#ciclo while solo terminara si el rut es correcto
    rut = input('Ingrese el rut: ')
    listaRut = [int(i) for i in rut if i.isdigit()]#rescata solo los numeeros del rut en una lista
    dv = rut[len(rut)-1]#variable solo el digito verificador
    if (dv.upper() == 'K'):#si el digito verificador el una K
        listaRut.append('K')#agrega una K al la listarut
    if (len(listaRut) == 8):#si el largo del rut es 8 agraga un 0 al principio
        listaRut.insert(0,'0')
    listaRut.insert(2,'.')#agrega un punto en el rut final
    listaRut.insert(6,'.')#agrega un punto en el rut final
    listaRut.insert(10,'-')#agrega un guion en el rut final
    i = 0#contador
    rutStr = []#declara una variable lista
    while(i < 12):#ciclo while para transformar todos los datos de la lista en str
        rutStr.append(str(listaRut[i]))
        i = i+1
    rutFinal =''.join(rutStr)#junta todos los casilleros de la lista en un solo str
    if (validateRut(rut) == True):#si el rut es valido imprime el rut
        print('El rut ingresado {} es Correcto'.format(rutFinal))
        salir = 1#hace q termine el ciclo while al ingresar un rut correcto
    else:#si el rut es incorrecto pide q lo ingrese denuevo
        print('El rut ingresado {} es Incorrecto, intentelo nuevamente'.format(rutFinal))
