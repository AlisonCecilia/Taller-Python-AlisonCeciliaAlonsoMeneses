if __name__ == '__main__':
    nom1=str(input("Proporciona un nombre: "))
    nom2=str(input("Proporciona el segundo nombre: "))

    #Es una funcion
    t1=len(nom1)
    t2=len(nom2)

    if t1==t2:
        print(f"Los nombres {nom1} y {nom2} son iguales")
    elif t1>t2:
        print("El nombre mas largo es ", nom1)
    else:
        print("El nombre mas largo es ", nom2)