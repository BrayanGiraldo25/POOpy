from persona import Persona
from estudiante import Estudiante
from profesor import Profesor


class Universidad:
    def __init__(self, nombreU):
        self.nombreU = nombreU
        self.estudiantes = {}  # Inicializar un diccionario vacío
        self.profesores = {}  # Diccionario para almacenar los profesores

    def agregar_Estudiante(self, estudiante: Estudiante):
        self.estudiantes[estudiante.nombre] = estudiante  # Guardar al estudiante usando su nombre como clave

    def agregar_Profesor(self, profesor: Profesor):
        self.profesores[profesor.nombre] = profesor  # Guardar al profesor usando su nombre como clave

    def imprimirEstudiante(self):
        print(f"\nUniversidad: {self.nombreU}\n")
        print("Estudiantes:")
        for est in self.estudiantes.values():
            print(
                f" - {est.imprimirDatosPer()} \n {est.imprimirDatosEst()}")  # Llamar los métodos correctamente con paréntesis

    def imprimirProfesor(self):
        print(f"\nProfesores en la Universidad: {self.nombreU}\n")
        for prof in self.profesores.values():
            # Llamar el método correctamente sobre la instancia 'prof'
            print(f" - {prof.ImprimirDatosTeacher()}")

