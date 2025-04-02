from persona import Persona
from estudiante import Estudiante
from profesor import Profesor
from universidad import Universidad

if __name__ == '__main__':
    estudiante1 = Estudiante(123, 'Pepe', 20, 'Desarrollo', ['Backend', 'POO', 'Agiles'])
    estudiante2 = Estudiante(456, 'Hugo', 35, 'Desarrollo', ['Backend', 'POO', 'Agiles'])
    profesor1 = Profesor(789, 'Duvan', 52, 'Ed.Fisica', ['07:00am', '10:20', '16:20'])

    uni = Universidad("CESDE")
    uni.agregar_Estudiante(estudiante1)
    uni.agregar_Estudiante(estudiante2)
    uni.agregar_Profesor(profesor1)

    #mostrar los metodos
    uni.imprimirEstudiante()
    uni.imprimirProfesor()
    pass