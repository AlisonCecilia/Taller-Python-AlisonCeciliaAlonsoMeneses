import json

if __name__ == '__main__':

    #version corta de abrir un archivo Json
    #Abre el archivo JSON en modo de lectura y with se encarga de cerrar

    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo) #Carga el contenido del archivo JSON

    for persona in datos["personas"]:
        print("Nombre:", persona["nombre"])
        print("Edad:", persona["edad"])
        print("Ciudad:", persona["ciudad"])
        print("Estado:", persona["estado"])
        print("-----------------------------")