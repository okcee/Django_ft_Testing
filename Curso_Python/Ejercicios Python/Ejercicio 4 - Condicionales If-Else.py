''' Ejercicios 4
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
'''
letra = input('Introduce una letra: ')
# if letra in 'aeiou':
#     print(f"La letra '{letra}' es una vocal.")
# else:
#     print(f"La letra '{letra}' no es una vocal.")

'''Explicación de la lista de comprensión:
[ ... for ... in ... if ... else ... ]: Esta es la estructura general de una lista de comprensión con una condición if-else.'''
print(f"La letra '{letra}' es una vocal." if letra in 'aeiou' else f"La letra '{letra}' no es una vocal.")

