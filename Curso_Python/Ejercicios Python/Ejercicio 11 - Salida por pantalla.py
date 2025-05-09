'''Ejercicio 11 - Salida por pantalla
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
'''

vocal = input('Introduce una vocal en minúscula: ')
letra = input('Introduce una letra en mayúscula: ')

print(f'La vocal en mayúscula es {vocal.upper()}')
print(f'La letra en minúscula es {letra.lower()}')
print(f'La concatenación de {vocal.upper()} y {letra.lower()} es {vocal.upper()+letra.lower()}')
