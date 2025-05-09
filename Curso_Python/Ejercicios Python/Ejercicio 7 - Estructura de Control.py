''' Ejercicio 7: Estructuras de control - Bucle For
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
'''
for i in range(1,11):
    print(i)

num_uno = int(input("Introduce un número entero: "))
num_dos = int(input("Introduce otro número entero: "))
numeros = []
for i2 in range(num_uno, num_dos+1):
    numeros.append(str(i2))

print(f'El rango de números enteros entre {num_uno} y {num_dos} es: ')
for numeros_i2 in numeros:
    print(numeros_i2)
