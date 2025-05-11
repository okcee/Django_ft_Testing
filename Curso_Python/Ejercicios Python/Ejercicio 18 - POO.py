''' Ejercicio 18: Programación Orientada a Objetos en Python
Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. Luego, se debe calcular area de un cuadrado, triangulo y pentagono
Área de un Cuadrado:    Área = l * l = l**2
Área de un Triángulo:   Área = ( b * h) / 2
    b es la longitud de la base del triángulo
    h es la altura del triángulo (la distancia perpendicular desde la base hasta el vértice opuesto)
Área de un Pentágono Regular:   Área = (P (Perímetro) x a (longitud de la apotema del pentágono regular)) / 2
    Para un pentágono regular con longitud de lado l, el perímetro P es 5*l.
    La apotema a se puede calcular mediante la fórmula: a = l / (2*tan(π/5)) o aprox. a≈l*0.688
'''
from math import pi, tan

class Areas:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    
    def cuadrado (self):
        return self.base**2
    
    def triangulo (self):
        return (self.base * self.altura)/2
    
    def pentagono (self):
        lado = self.base
        apotema =  lado / (2*tan(pi/5))
        return ((5 * lado) * apotema ) / 2
    
    def __str__ (self):
        res_cuadrado = self.cuadrado()
        res_triangulo = self.triangulo()
        res_pentagono = self.pentagono()
        output_lines = [
            f'Resultados para los valores de base = {self.base} y altura = {self.altura}:',
            f'  - El área de un cuadrado (lado = {self.base}) es: {res_cuadrado}',
            f'  - El área de un triángulo (base = {self.base}, altura={self.altura}) es: {res_triangulo}',
            f'  - El área de un pentágono regular (lado= {self.base}) es: {res_pentagono}'
        ]
        return "\n".join(output_lines)

print(Areas(10, 15))