''' Ejercicios 4.1
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

'''Ejercicio 4.2
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
'''
palabra_uno = input('Escribe una palabra: ')
palabra_dos = input('Escribe otra palabra: ')
if len(palabra_uno) < 3 or len(palabra_dos) < 3:
    print('Las palabras tienen que tener al menos 3 caracteres')
elif palabra_uno[-3:] == palabra_dos[-3:]:
    print(f'La palabra {palabra_uno} y la palabra {palabra_dos} riman')
elif palabra_uno[-2:] == palabra_dos[-2:]:
    print(f'La palabra {palabra_uno} y la palabra {palabra_dos} riman un poco')
else:
    print(f'La palabra {palabra_uno} y la palabra {palabra_dos} NO riman')
