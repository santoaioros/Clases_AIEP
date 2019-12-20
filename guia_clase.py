class guia_clase:
    def fullName(self,salir):
        name = input('Ingrese nombre: ')
        lastname = input('Ingrese apellido: ')
        print('Su nombre completo es : ' + name + ' ' + lastname)
        salir = 's'
        return salir

prueba = guia_clase()
print prueba.fullName()