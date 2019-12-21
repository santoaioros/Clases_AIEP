#class rut_main:
import os

def banner_correcto():
    print('╔════════════════════════════════╗')
    print('║El rut ingresado es CORRECTO ♥  ║')

def banner_incorrecto():
    print('╔════════════════════════════════╗')
    print('║El rut ingresado es INCORRECTO X║')

def validateRut (rut):
    #print (len(rut))
    dv = rut[len(rut)-1]
    #print(dv)
    numbers_list = [int(i) for i in rut[:-1] if i.isdigit()]
    #print (numbers_list)
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
cont_salir = 0
while(cont_salir==0):
    rut = input('Ingrese el rut: ')
    digit = [int(i) for i in rut if i.isdigit()]
    dv = rut[len(rut)-1]
    if (dv.upper() == 'K'):
        digit.append('K')
    if (validateRut(rut) == True):
        if(len(digit)==9):
            banner_correcto()
            print('║ '+str(digit[0])+str(digit[1])+'.'+str(digit[2])+str(digit[3])+str(digit[4])+'.'+str(digit[5])+str(digit[6])+str(digit[7])+'-'+str(digit[8])+'                   ║')
            print('╚════════════════════════════════╝')
        else:
            banner_correcto()
            print('║  '+str(digit[0])+'.'+str(digit[1])+str(digit[2])+str(digit[3])+'.'+str(digit[4])+str(digit[5])+str(digit[6])+'-'+str(digit[7])+'                   ║')
            print('╚════════════════════════════════╝')
        cont_salir = 1
    else:
        if(len(digit)==9):
            banner_incorrecto()
            print('║ '+str(digit[0])+str(digit[1])+'.'+str(digit[2])+str(digit[3])+str(digit[4])+'.'+str(digit[5])+str(digit[6])+str(digit[7])+'-'+str(digit[8])+'                   ║')
            print('╚════════════════════════════════╝')
        else:
            banner_incorrecto()
            print('║  '+str(digit[0])+'.'+str(digit[1])+str(digit[2])+str(digit[3])+'.'+str(digit[4])+str(digit[5])+str(digit[6])+'-'+str(digit[7])+'                   ║')
            print('╚════════════════════════════════╝')
os.system("Pause")        

#numbers_list = numbers_list[::-1]
#print(numbers_list)

