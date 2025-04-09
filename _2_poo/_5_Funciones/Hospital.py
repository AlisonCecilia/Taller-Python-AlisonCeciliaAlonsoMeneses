class Hospital:
    def __init__(self):
        self.__NombrePaciente:str=""
        self.__nss:int=1258
        self.__enfermedad:str=""

    def __getNombrePaciente(self)->str:
        return self.__NombrePaciente

    def getNss(self)->int:
        return self.__nsss

    @property #ESto convierte el estado en una proiedad de solo lectura
    def getEfermedad(self)->str:
        return self.enfermedad

    def getNombrePaciente(self, nombre:str):
        self.NombrePaciente=nombre

    def getNss(self, nss:int):
        self.nss=nss

    #@dosis_hora.setter #Esto convierte el metodo en una propiedad de solo lectura
    def getEfermedad(self, enfermedad= str):
        self.enfermedad=enfermedad



if __name__ == '__main__':
    hospital=Hospital()
    hospital.__NombrePaciente="Juan"
    print(hospital.__getNombrePaciente)