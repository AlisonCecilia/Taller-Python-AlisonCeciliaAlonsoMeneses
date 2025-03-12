import sys
# from os.path import split
# from os.path import join


if __name__ == '__main__':
    print("rango de 0 ")
    for i in range(10):
        print(f"{i}")

    print("rango de 6 a 11")
    for i in range(6,12):
        print(f"{i}")

    print("rango de 6 a 11 pero con incrementos de")
    for i in range(6,12,3):
        print(f"{i}", end=" ")

    sys.stdout.write("Texto sin salto de linea")
