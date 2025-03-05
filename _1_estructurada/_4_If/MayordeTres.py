if __name__ == '__main__':
    a=int(input("Proporcion un numero: "))
    b=int(input("Proporcion otro numero: "))
    c=int(input("Proporcion un ultimo numero: "))

    if a>b:
        if a>c:
            print(f"el mayor es {a}")
        else:
            print(f"El mayor es {a}")
    else:
        if b>c:
            print(f"el mayor es {b}")
        else:
            print(f"El mayor es {c}")



