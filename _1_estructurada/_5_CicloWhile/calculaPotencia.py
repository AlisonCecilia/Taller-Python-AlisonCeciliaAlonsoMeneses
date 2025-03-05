if __name__ == '__main__':
    x=int(input("ingresa un numero: "))
    y=int(input("ingresa la potencia: "))

    i:int=0
    pot:int=1

    while i<y:
        pot=pot*x
        i=i+1

    # f para incrustamiento
    print(f"El resulta de {x}^{y}={pot}")