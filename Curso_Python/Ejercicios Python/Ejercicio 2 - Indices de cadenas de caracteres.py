''' Ejercicio 2
En la siguiente lista, debes de hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]
'''
lista = [20, 50, "Curso", 'Python', 3.14]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
val_uno = input("Ingrese el primer valor a modificar: ")
val_dos = input("Ingrese el segundo valor a modificar: ")
lista[0] = val_uno
lista[1] = val_dos
print(lista)