class Auto:
    marca= "Honda" #Esto es un atributo de la clase Auto
    modelo=1000 #Esto es un atributo de la clase Auto
    placa="PCH-96-04" #Esto es un atributo de la clase Auto

if __name__ == '__main__':
    taxi= Auto() #ESto es una insstanica de la clase Archivo
    miauto=Auto() #ESto es otra insstanica de la misma clase Archivo

    print(taxi.placa) #Se ivoca no de los atributos delaclase
    miauto.placa="TCV-963-12"
    print(miauto.placa)