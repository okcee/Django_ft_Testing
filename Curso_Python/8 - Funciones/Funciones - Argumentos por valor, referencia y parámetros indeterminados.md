# Funciones en Python
Las funciones son bloques de código reutilizables que realizan una tarea específica. Permiten organizar el código, hacerlo más legible y evitar la repetición.

## Definición de una Función
En Python, una función se define utilizando la palabra clave `def`, seguida del nombre de la función, paréntesis `()` que pueden contener parámetros, y dos puntos `:`. El cuerpo de la función se define con indentación.

```python
def saludar(nombre):
    """Esta función saluda a la persona que se pasa como parámetro."""
    print(f"Hola, {nombre}!")

# Llamada a la función
saludar("Mundo")
'''
def: Palabra clave para definir una función.
saludar: Nombre de la función.
(nombre): Parámetro que recibe la función.
"""Docstring""": Cadena de documentación que explica qué hace la función.
print(...): Cuerpo de la función
'''
```

## La Sentencia `return`
La sentencia `return` se utiliza para salir de una función y, opcionalmente, devolver un valor. Si una función no tiene `return` o tiene un `return` sin valor, devuelve `None` por defecto.
```python
def sumar(a, b):
  """Esta función suma dos números y devuelve el resultado."""
  resultado = a + b
  return resultado

# Llamada a la función y almacenamiento del resultado
suma_total = sumar(5, 3)
print(f"La suma es: {suma_total}")
```

## Argumentos en Python: Paso por "Referencia al Objeto"
A diferencia de otros lenguajes que tienen un paso explícito por valor o por referencia, Python utiliza lo que se describe mejor como "paso por referencia al objeto" (pass by object reference). Esto significa que cuando pasas un argumento a una función, lo que se pasa es una referencia al objeto en memoria al que apunta la variable.  

El comportamiento dentro de la función dependerá de si el objeto pasado es mutable (su estado puede cambiar) o inmutable (su estado no puede cambiar una vez creado).  

```python
def modificar_numero(numero):
  """Intenta modificar un número (inmutable)."""
  numero = numero + 10
  print(f"Dentro de la función (número): {numero}")

mi_numero = 5
modificar_numero(mi_numero)
print(f"Fuera de la función (mi_numero): {mi_numero}") # Salida: 5
'''
En este caso, mi_numero fuera de la función sigue siendo 5 porque la modificación dentro de modificar_numero creó un nuevo objeto entero local.
'''
```

## Comportamiento con Tipos Mutables (como list, dict, set)
Cuando pasas un objeto mutable a una función y modificas su contenido dentro de la función, estos cambios sí afectarán al objeto original fuera de la función, ya que ambas variables (la original y la de la función) apuntan a la misma posición en memoria.  
```python
def modificar_lista(lista):
  """Modifica una lista (mutable)."""
  lista.append(4)
  print(f"Dentro de la función (lista): {lista}")

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(f"Fuera de la función (mi_lista): {mi_lista}") # Salida: [1, 2, 3, 4]
'''
Aquí, mi_lista fuera de la función se modifica porque append() opera directamente sobre el objeto de lista al que apunta la referencia.
'''
```

Importante: Si dentro de la función reasignas la variable que apunta a un objeto mutable a un nuevo objeto, la variable original fuera de la función no se verá afectada por esa reasignación.
```python
def reasignar_lista(lista):
  """Reasigna la variable local a una nueva lista."""
  lista = [5, 6, 7]
  print(f"Dentro de la función (lista): {lista}")

otra_lista = [1, 2, 3]
reasignar_lista(otra_lista)
print(f"Fuera de la función (otra_lista): {otra_lista}") # Salida: [1, 2, 3]
```

## Parámetros Indeterminados (*args y **kwargs)
Python permite definir funciones que pueden aceptar un número variable de argumentos utilizando *args y **kwargs.

### Argumentos Posicionales Indeterminados (*args)
El uso de `*args` en la definición de una función permite que la función acepte un número cualquiera de argumentos posicionales. Estos argumentos se empaquetan en una tupla dentro de la función. Por convención, se utiliza el nombre `args`, pero se puede usar cualquier otro nombre precedido por un asterisco.  
```python
def suma_indeterminada(*numeros):
  """Suma un número indeterminado de argumentos."""
  total = 0
  for numero in numeros:
    total += numero
  return total

print(suma_indeterminada(1, 2, 3))         # Salida: 6
print(suma_indeterminada(10, 20, 30, 40)) # Salida: 100
'''
Dentro de suma_indeterminada, numeros es una tupla que contiene los argumentos pasados.
'''
```

### Argumentos con Nombre Indeterminados (**kwargs)
El uso de `**kwargs` en la definición de una función permite que la función acepte un número cualquiera de argumentos con nombre (palabra clave). Estos argumentos se empaquetan en un diccionario dentro de la función, donde las claves son los nombres de los argumentos y los valores son los valores pasados. Por convención, se utiliza el nombre `kwargs`, pero se puede usar cualquier otro nombre precedido por dos asteriscos.  
```python
def mostrar_info(**datos):
  """Muestra información pasada como argumentos con nombre."""
  for clave, valor in datos.items():
    print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Madrid")
'''
Dentro de mostrar_info, datos es un diccionario como {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Madrid'}.
'''
```

### Combinando Argumentos
Puedes combinar argumentos posicionales normales, *args, y **kwargs en una misma definición de función. El orden debe ser:  
    1. Argumentos posicionales normales.
    2. `*args`.
    3. Argumentos con nombre normales (con valor por defecto o no).
    4. `**kwargs`.
```python
def funcion_completa(arg1, arg2, *args, kwarg1, **kwargs):
  print(f"arg1: {arg1}")
  print(f"arg2: {arg2}")
  print(f"args: {args}")
  print(f"kwarg1: {kwarg1}")
  print(f"kwargs: {kwargs}")

funcion_completa(1, 2, 3, 4, 5, kwarg1="valor1", nombre="Pepe", edad=25)
```

En resumen, las funciones son herramientas fundamentales para estructurar código en Python. La forma en que se pasan los argumentos se basa en referencias a objetos, con el comportamiento de modificación dependiendo de la mutabilidad del objeto. Los parámetros `*args` y `**kwargs` ofrecen flexibilidad para trabajar con un número variable de argumentos posicionales y con nombre, respectivamente.  
