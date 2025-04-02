from persona import Persona

class Profesor(Persona):
    def __init__(self, identificacion: int, nombre: str, edad: int, area: str, horarios: list):
        super().__init__(identificacion, nombre, edad)
        self.area = area
        self.horarios = horarios

    def ImprimirDatosTeacher(self):
        return f"Datos Teacher\nÁrea que maneja: {self.area}\nHorario: {'\n - '.join(self.horarios)}"