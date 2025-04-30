''' Ejercicio 1
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
• Imprima los dos primeros caracteres.
• Imprima los tres últimos caracteres.
• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''

mensaje = 'Te quiero solo como amigo'
print("Dos primeros caracteres: ", mensaje[0:3]) # Te 
print("Tres últimos caracteres caracteres: ", mensaje[-3:]) # igo
print("Dicha cadena cada dos caracteres: ", mensaje[::2]) # T ueosl ooaio
print("Dicha cadena en sentido inverso: ", mensaje[::-1]) # ogima omoc olos oreiuq eT
print("Cadena en un sentido y en sentido inverso: ", mensaje+" "+mensaje[::-1]) # Te quiero solo como amigo ogima omoc olos oreiuq eT
