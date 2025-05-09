'''Ejercicio 5
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
