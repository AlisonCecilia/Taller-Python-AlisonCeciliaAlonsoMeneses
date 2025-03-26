from itertools import count

if __name__ == '__main__':
    agenda={}

    agenda["GUAT800717"]=("Tomas Gonzales", "csctomasgonzales@gmail.com", "2222001")
    agenda["GUAT800718"] = ("Luis Gonzales", "luis85@gmail.com", "2222002")
    agenda["GUAT800719"] = ("Fabiola Gonzales", "fabis25@gmail.com", "2222003")
    agenda["GUAT800716"] = ("Fernando Gonzales", "fergon@gmail.com", "2222004")

    nombre,correo,numero=agenda["GUAT800717"]


    print(f"Datos de la persona: {nombre}, {correo}, {numero}")

