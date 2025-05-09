''' Ejercicio 6: Estructuras de control - Bucle While
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''

numero = int(input("Ingrese un número entero: "))
i = 0
multi = 0

print(f'La tabla de multiplicar del número {numero} es:')
while i <= 10:
    multi = numero * i
    print(f'{numero} x {i} = {multi}')
    i += 1

