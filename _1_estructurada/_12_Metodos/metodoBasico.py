import statistics as mate
#def suma(a:int,b:int):
 #   print(f"La suma de {a} + {b} es {a+b}")

def suma (a:int, b=None,c=None):
    if b is None:
        print(f"{a}")
    elif c is None:
        print(f"La suma de {a} + {b} es {a+b}")
    else:
        print(f"La suma de {a} + {b} + {c} es {a + b + c}")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=mate.mean(lista)
    print(f"El promedio es {p}")

if __name__ == '__main__':
    suma(15)
    suma(45)
    suma(55)

    suma(6,4)
    suma(10,5)
    suma(10,52)

    suma(23, 47,20)
    suma(12,255,25)
    suma(5,5,20)

    lista2=[1,2,3,4,5]
    promedioArreglo(lista2)
    print(lista2)