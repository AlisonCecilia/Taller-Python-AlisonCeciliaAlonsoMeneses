from unicodedata import numeric

if __name__ == '__main__':

    try:
        # Codigo que puede cusar una excepcion
        numero=int(input("Introduce un numero: "))
        resultado= 18/numero
    except ValuaError:
        # Maneja de la excepion si se introduce un valor no valido
        print("¡Error! Debes introducir un numero entero.")
    except ZeroDivisionError:
        # Maneja de la excepcion si se intenta dividri por cero
        print("¡Error! No se puede dividir entre cero.")
    else:
        # Se ejecuta si no hubo excepciones
        print("El resultado es:", resultado)
    finally:
        # Se ejecuta si no hub excepciones
        print("Fin del programa.")