class Persona:
    def __init__(self, identificacion, nombre, edad):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad

    def imprimirDatosPer(self):
        return f"Datos Personas\nIdentificacion: {self.identificacion}\nNombre: {self.nombre}\nEdad: {self.edad}"