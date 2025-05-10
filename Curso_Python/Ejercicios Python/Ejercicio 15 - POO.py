''' Ejercicio 15: Programación Orientada a Objetos en Python
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''

class Alumno: # Se inicia la clase Alumno
    def __init__(self, nombre, nota): # Se definen como parámetros "nombre" y "nota"
        self.nombre = nombre # str
        try: # Se crea un bloque para pasar la nota a dato tipo "float" y hacer una validación del mismo
            self.nota = float(nota) 
        except ValueError:
            print(f"Advertencia: La nota '{nota}' proporcionada para {self.nombre} no es un número válido.")
        except TypeError:
            print(f"Advertencia: Tipo de nota inválido para {self.nombre}.")
    
    def __str__(self):
        return f"Alumno: {self.nombre}, Nota: {self.nota}"
    
    def calificación(self,):
        try:
            if self.nota < 5 and self.nota > 0:
                print(f'Estudiante {self.nombre} sacó de nota {self.nota}, por lo que suspendió.', '\n')
            elif self.nota >= 5 and self.nota <= 10:
                print(f'Estudiante {self.nombre} sacó de nota {self.nota}, por lo que aprobó.', '\n')
            else:
                print('El valor de nota no está entre los valores 0 y 10', '\n')
        except Exception as e:
            return print({e})

# Ejemplos de uso:
alumno1 = Alumno('Carlos', 4.2)
print(alumno1)  # Esto llamará a __str__
alumno1.calificación() # Esto mostrará si está aprobado o suspenso

alumno2 = Alumno('Clara', 7.1)
print(alumno2)
alumno2.calificación()

alumno3 = Alumno('Francisco', 22)
print(alumno3)
alumno3.calificación()

alumno4 = Alumno('Samuel', 5.00)
print(alumno4)
alumno4.calificación()

alumno5 = Alumno('Dayanne', 7.97)
print(alumno5)
alumno5.calificación()