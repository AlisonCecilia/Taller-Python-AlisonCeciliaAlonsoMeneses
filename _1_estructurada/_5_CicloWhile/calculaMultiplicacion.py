if __name__ == '__main__':
    x = int(input("ingresa un numero: "))
    y = int(input("ingresa el segundo numero: "))

    i: int = 0
    mut: int = 0

    while i < y:
        mut= mut + x#multiplicacion por suma
        i = i + 1

    # f para incrustamiento
    print(f"El resulta de {x}x{y}={mut}")