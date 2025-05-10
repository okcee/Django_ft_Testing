''' Ejercicio 16: Programación Orientada a Objetos en Python
Escribir una clase en python que calcule pow(x, n)
    x = es la base
    n = es el exponente
'''
'''
Explicación completa de isinstance()
La función isinstance() es la forma recomendada en Python para verificar el tipo de un objeto, especialmente porque maneja correctamente la herencia.

isinstance(object, classinfo)
object: Es el objeto cuyo tipo quieres verificar.
classinfo: Puede ser:
    - Un tipo incorporado (por ejemplo, int, str, list, dict, float, bool, tuple, set).
    - Una clase que hayas definido tú (por ejemplo, Alumno, Potencia en tus ejercicios).
    - Una tupla de tipos y/o clases. Si proporcionas una tupla, isinstance() devolverá True si el object es una instancia de cualquiera de los elementos en la tupla. Por ejemplo: (int, float) o (str, list, MiClase).

Valor de retorno:
    - Devuelve True si object es una instancia de classinfo o si object es una instancia de una subclase de classinfo.
    - Devuelve False en caso contrario
'''
class ErrorDeTipoPotencia(ValueError): # Excepción personalizada para errores de tipo
    pass

class Potencia: # Clase Potencia (Calcula la potencia de un número)
    def __init__ (self, x, n): # Se aceptan x y n como argumentos directos
        self.x = x # Se inicia el número base tal y como se recibe
        self.n = n # Este es el índice de la potencia
    
    def validacion (self):
        try:
            if not isinstance(self.x, (int, float)):
                raise ErrorDeTipoPotencia(f"Error: La base ('{self.x}') debe ser un número.")
            elif not isinstance(self.n, (int, float)):
                raise ErrorDeTipoPotencia(f"Error: El exponente ('{self.n}') debe ser un número.")
            else:
                return self
        except Exception as e:
            print (f"Error en validación: {e}") # Formato para el mensaje de error
    
    def calculo (self): # Se define un método para realizar el cálculo
        # Primero, verificamos si la base y el exponente son numéricos
        if not isinstance(self.x, (int, float)):
            raise ErrorDeTipoPotencia(f"Error: La base ('{self.x}') debe ser un número.\n")
        if not isinstance(self.n, (int, float)):
            raise ErrorDeTipoPotencia(f"Error: El exponente ('{self.n}') debe ser un número.\n")
        
        # Si ambos son numéricos, procedemos con el cálculo
        return pow(self.x, self.n) # pow() puede aún lanzar errores (ej. 0**-1), pero no por tipo str
    
    def __str__(self): # Se define el método "str" para devolver una cadena de texto tipo "string"
        try:
            resultado_calculo = self.calculo()
            return f'La potencia {self.n} del número {self.x} es: {resultado_calculo}\n'
        except ErrorDeTipoPotencia as e:
            return str(e) # Devuelve solo el mensaje de la excepción

potencia1 = Potencia(2, 2)
print(potencia1)

potencia2 = Potencia(5, 3)
print(potencia2)

potencia_con_error = Potencia("base_texto", 2) # Ejemplo con base no numérica
print(potencia_con_error)

exponente_con_error = Potencia(2, "exponente_texto") # Ejemplo con exponente no numérico
print(exponente_con_error)
