''' Ejercicio 13: Funciones
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
'''

def comparar():
    num_uno = 0
    num_dos = 0
    num_uno = int(input('Indroduca el primer número a comparar: '))
    num_dos = int(input('Indroduca el segundo número a comparar: '))
    if num_uno > num_dos:
        return 1
    elif num_uno < num_dos:
        return -1
    else:
        return 0
print(comparar())
