''' Ejercicio 12: Funciones
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas
'''
lista = []
num = 0

def añadir():
    numeros = int(input('Cuántos números vas a querer añadir a la lista\n'))
    n = 0
    while n < numeros:
        num = float(input("Introduzca un número: "))
        lista.append(num)
        n+=1
    return lista

def ordenar():
    lista.sort()
    pares = []
    impar = []
    for i in lista:
        if i%2 == 0:
            pares.append(i)
        else:
            impar.append(i)
    print(f' Los numeros pares son: {pares}')
    print(f' Los numeros impares son: {impar}')

# --- Aquí es donde llamas a las funciones ---
añadir()
ordenar()