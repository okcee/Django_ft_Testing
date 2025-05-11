''' Ejercicio 19: Programación Orientada a Objetos en Python
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.
Herencia
'''

class Fabrica():
    def __init__ (self, Llantas, Color, Precio):
        self.Llantas = Llantas
        self.Color = Color
        self.Precio = Precio

class Moto(Fabrica):
    def datos(self):
        print(f'La cantidad de llantas de la moto es de: {self.Llantas}')
        print(f'El color de la moto es de: {self.Color}')
        print(f'El precio de la moto es de: {self.Precio}€\n')

class Carro(Fabrica):
    def datos(self):
        print(f'La cantidad de llantas del carro es de: {self.Llantas}')
        print(f'El color del carro es de: {self.Color}')
        print(f'El precio del carro es de: {self.Precio}€\n')

moto = Moto(2, 'Negro', 4000)
moto.datos()

carro = Carro(4, 'Blanco', 23000)
carro.datos()
