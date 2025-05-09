''' Ejercicio 10: Entrada por teclado
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

x = (-b + math.sqrt(pow(b, 2) - (4*a*c))) / (2 * a)
'''
import math
import cmath # Para manejar raíces cuadradas de números negativos

# Define los coeficientes a, b, c de tu ecuación
try:
    a_str = input('Ingrese el coeficiente a: ')
    a = float(a_str)

    b_str = input('Ingrese el coeficiente b: ')
    b = float(b_str)

    c_str = input('Ingrese el coeficiente c: ')
    c = float(c_str)

    lista = [a, b, c]

except ValueError:
    print("Entrada inválida. Por favor, ingrese números válidos para los coeficientes.")
    exit() # Sale del programa si la conversión falla



# --- Calculamos el discriminante (el valor dentro de la raíz cuadrada) ---
discriminante = pow(b, 2) - (4 * a * c)

# --- Ahora calculamos las raíces basándonos en el valor del discriminante ---
# Primero, verificamos si a es 0. Si lo es, no es una ecuación cuadrática.
if a == 0:
    print("El coeficiente 'a' es 0. No es una ecuación cuadrática.")
    # Si b tampoco es 0, es una ecuación lineal: bx + c = 0 => x = -c/b
    if b != 0:
        x_lineal = -c / b
        print(f"Es una ecuación lineal con una raíz: x = {x_lineal}")
    elif c == 0:
        print("La ecuación es 0 = 0. Infinitas soluciones.")
    else:
        print("La ecuación es una constante distinta de 0. No hay solución.")

# Si a no es 0, procedemos con la fórmula cuadrática
else:
    print(f"Resolviendo la ecuación cuadrática: {a}x^2 + {b}x + {c} = 0")
    print(f"Discriminante (b^2 - 4ac): {discriminante}")

    # Caso 1: Discriminante >= 0 (Raíces reales, distintas o iguales)
    if discriminante >= 0:
        print("El discriminante es >= 0. Las raíces son reales.")

        # Calculamos la raíz cuadrada del discriminante usando math.sqrt (para números reales)
        raiz_discriminante = math.sqrt(discriminante)

        # Aplicamos la fórmula para las dos raíces: una con + y otra con -
        # Raíz 1 (usando el +)
        x1 = (-b + raiz_discriminante) / (2 * a)

        # Raíz 2 (usando el -)
        x2 = (-b - raiz_discriminante) / (2 * a)

        # Si el discriminante es 0, las raíces son iguales
        if discriminante == 0:
            print("Las raíces son reales e iguales.")
            print(f"Raíz única: x = {x1}") # x1 y x2 serán el mismo valor
        else: # discriminante > 0
            print("Las raíces son reales y distintas.")
            print(f"Raíz 1 (usando +): x1 = {x1}")
            print(f"Raíz 2 (usando -): x2 = {x2}")


    # Caso 2: Discriminante < 0 (Raíces complejas)
    else:
        print("El discriminante es < 0. Las raíces son complejas.")

        # Calculamos la raíz cuadrada del discriminante usando cmath.sqrt (para números complejos)
        # La raíz de un número negativo será un número imaginario (ej: sqrt(-9) = 3j)
        raiz_discriminante_compleja = cmath.sqrt(discriminante)

        # Aplicamos la fórmula para las dos raíces complejas
        # Raíz 1 (usando el +)
        x1_compleja = (-b + raiz_discriminante_compleja) / (2 * a)

        # Raíz 2 (usando el -)
        x2_compleja = (-b - raiz_discriminante_compleja) / (2 * a)

        print("Las raíces son complejas y conjugadas.")
        print(f"Raíz 1 (usando +): x1 = {x1_compleja}")
        print(f"Raíz 2 (usando -): x2 = {x2_compleja}")
        # Las raíces complejas se mostrarán en el formato (parte_real + parte_imaginaria j)
