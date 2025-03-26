if __name__ == '__main__':

    diccionario={
        ("id","int"): '2',
        'nombre':'Juan',
        'apellido':'Gutierres'
    }

    diccionario={}

    #Agregar tupla como clave
    diccionario[("Ana",25)]="Estudiante"
    diccionario[("Luis", 30)] = "Ingenierio"
    diccionario[("Carlos", 40)] = "Abogado"

    #Acceder a los valores del diccionariousando la tupla
    ocupacion_ana=diccionario[("Ana",25)]
    ocupacion_luis=diccionario[("Luis",30)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_luis}")