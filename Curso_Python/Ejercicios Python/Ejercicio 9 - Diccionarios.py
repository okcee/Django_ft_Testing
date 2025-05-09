''' Ejercicio 9: Conjunto de datos - Diccionario
En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

print('''
    Escoge y ecribe uno de los siguientes países para saber su capital:
        - Guatemala
        - El Salvador
        - Honduras
        - Nicaragua
        - Costa Rica
        - Panama
        - Argentina
        - Colombia
        - Venezuela
        - España
    ''')
pais = input()
print(f'La capital de {pais} es: {diccionario[pais]}')