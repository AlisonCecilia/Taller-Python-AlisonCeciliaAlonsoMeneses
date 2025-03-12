if __name__ == '__main__':
    print ("------------------------------------------")
    lista=[1,2,3,4,"Lunes",5,6,7,8,9,10,11,12,13,14,15,16]
    #Una lista puede contener valores de diferente tipo
    #Ademas una lista es mutable

    lista.append(200)
    lista.append("Viernes")
    lista.append(False)
    lista.append(2.69)

    lista2=[1200,1300,1500]
    lista.append(lista2)

    for elemento in lista:
        print(elemento)

    lista2=[17,18,19,20]
    lista.extend(lista2)

    nombre:str
    nombre="Luis"
    nombre +="Gutierrez"
    nombre.join("Gutierrez")

    lista3=["Alfredo","Pablo","Karla"]
    cadena:str=" - ".join(lista3)#La funcion joim se utiliza para
    print(cadena)

    separado=cadena.split()#Split s eutiliza para separar las
    for dato in separado:
        print(dato)