def suma (a:int,b:int)->int:
    return a+b

def sumaArreglo(lista:list)->int:
    return sum(lista)

if __name__ == '__main__':
    print(f"La suma es {suma(15,22)}")

    print(f"La suma del arrelo es {sumaArreglo([5,9,1,3,12])}")
