class rut_clase:    
    rut = input('ingrese rut: ')
    def rut_metodo (listaFinal):
        lista = [self.rut]
        lista.insert(2,'.')
        lista.insert(6,'.')
        lista.insert(10,'-')
        i=0
        listaStr =[]
        while(i<12):
            listaStr.append(str(lista[i]))
            i=i+1
        listaFinal =''.join(listaStr)
        return (listaFinal)
    rut_listo = rut_metodo()
    print(rut_listo)
