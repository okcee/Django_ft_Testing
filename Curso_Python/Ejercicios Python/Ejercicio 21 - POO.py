''' Ejercicio 21: Programación Orientada a Objetos en Python
Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
Herencia Múltiple
'''

class Universidad():
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera():
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera): # Hereda de la clase corregida
    # El constructor ahora toma todos los datos necesarios
    def __init__(self, nombre_estudiante, edad_estudiante, nombre_universidad, especialidad_carrera):
        # Inicializar la parte de Universidad
        Universidad.__init__(self, nombre_universidad)
        # Inicializar la parte de Carrera
        Carrera.__init__(self, especialidad_carrera)
        # Inicializar los atributos propios de Estudiante
        self.nombre = nombre_estudiante
        self.edad = edad_estudiante
        
        print(f'Mi nombre es {self.nombre}, tengo {self.edad} años, mi especialidad es {self.especialidad}. Estudio en la Universidad {self.Nombre}')


persona = Estudiante('Paca', 20, 'Cambridge', 'Economía')

