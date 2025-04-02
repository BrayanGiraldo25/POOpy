from persona import Persona

class Estudiante(Persona):

    def __init__(self, identificacion:int, nombre:str, edad:int, carrera:str, materias:list):
        super().__init__(identificacion, nombre, edad)
        self.carrera = carrera
        self.materias = materias

    def imprimirDatosEst(self):
        return f"Programa: {self.carrera}\nMaterias: {'\n - '.join(self.materias)}"