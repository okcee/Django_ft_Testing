''' Ejercicio 9: Conjunto de datos - Diccionario
En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

# print('''
#     Escoge y ecribe uno de los siguientes países para saber su capital:
#         - Guatemala
#         - El Salvador
#         - Honduras
#         - Nicaragua
#         - Costa Rica
#         - Panama
#         - Argentina
#         - Colombia
#         - Venezuela
#         - España
#     ''')
# pais = input()
# print(f'La capital de {pais} es: {diccionario[pais]}')

'''Manera que convierte la primera letra de cada palabra a mayúscula'''
# Solicitar al usuario que ingrese un país
pais_ingresado = input("Ingrese un país para saber su capital: ")

# Normalizar la entrada del usuario para que coincida con las claves del diccionario.
# Usamos .title() para que cada palabra comience con mayúscula (ej: "costa rica" -> "Costa Rica").
# Esto es importante porque las claves en el diccionario tienen este formato.
pais_clave = pais_ingresado.title()

# Verificar si el país (ya normalizado) se encuentra en el diccionario.
# La variable 'encontrado' será True si pais_clave es una de las claves del diccionario, y False en caso contrario.
encontrado = pais_clave in diccionario

# Comprobar si se encontró el país
if encontrado: # Esta es la forma idiomática en Python de verificar si un booleano es True.
    # Si se encontró, mostrar la capital.
    # Usamos 'pais_ingresado' (la entrada original) para el mensaje al usuario,
    # y 'pais_clave' (la entrada normalizada) para buscar en el diccionario.
    print(f'La capital de {pais_ingresado} es: {diccionario[pais_clave]}')
else:
    # Si no se encontró, mostrar un mensaje indicándolo.
    # Incluimos el país ingresado por el usuario para mayor claridad.
    print(f'El país "{pais_ingresado}" no está en el diccionario de capitales.')