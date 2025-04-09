class Datos:
    def __init__(self, nombre, correo, whatsapp):
        self.nombre= nombre
        self.correo= correo
        self.whatsapp= whatsapp

    def setNombre(self, nombre:str):
        self.nombre=nombre

if __name__ == '__main__':
    datos: Datos('Tomas','hjkdfhj@gmail.com',2481968948)

    print(datos.nombre)
    datos.setNombre("Juan")
    print(datos.nombre)
    datos.nombre="Gabriela"
    print(datos.nombre)