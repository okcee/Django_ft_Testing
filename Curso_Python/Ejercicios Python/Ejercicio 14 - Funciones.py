''' Ejercicio 14: Funciones
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
¬ Área de un Cuadrado:  Área = base × altura
¬ Área de un Círculo:   Área = π × radio**2
Donde π (pi) es una constante matemática aproximadamente igual a 3.14159. En Python, puedes obtener un valor más preciso de π desde el módulo math (math.pi).
'''
# Programa de funciones de área

from math import pi

def cuadrado (base=float, altura=float):
    area_cuadrado = base * altura
    return area_cuadrado

def circulo (radio):
    area_circulo = pi * pow(radio, 2)
    return area_circulo


print('El área de un cuadrado es: ', cuadrado(20.6, 35.8))
print('El área de un cuadrado es: ', cuadrado(10, 5))
print('\n',pi, '\n')
print('El área de un círculo es: ', circulo(29.0))
print('El área de un círculo es: ', circulo(10))