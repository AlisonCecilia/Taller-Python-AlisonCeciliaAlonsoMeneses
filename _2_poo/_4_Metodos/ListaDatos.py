class ListaDatos:

    def __init__(self,matriula:str,estudiante:str,asignatura:str):
        self.matricula= matriula
        self.estudiante= estudiante
        self.asignatura= asignatura

if __name__ == '__main__':
    lista = []
    lista.append(ListaDatos("22240057", "Alison Alonso", "POO"))
    lista.append(ListaDatos("22240041", "Alfredo Morales", "POO"))
    lista.append(ListaDatos("22240059", "Elsi Mendez", "POO"))
    lista.append(ListaDatos("22240001", "Dulce Barragan", "POO"))
    lista.append(ListaDatos("22240060", "Tomas Diaz", "POO"))

    for obj in lista:
        print(f"Matricula: {obj.matricula}")
        print(f"Estudiante: {obj.estudiante}")
        print(f"Asignatura: {obj.asignatura}")
        print("-------------------------------------")