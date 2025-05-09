''' Ejercicio 8: Conjunto de datos - Tuplas
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla
'''
meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
num = int(input("Introduce el número del mes para saber a cuál corresponde (Entre 1 - 12)"))

print(f'El mes {num} es {meses[num-1]}')
