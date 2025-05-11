''' Ejercicio 17: Programación Orientada a Objetos en Python
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''

class Calculadora:
    def __init__(self, valor1, valor2):
        try:
            self.valor1 = int(valor1)
            self.valor2 = int(valor2)
        except ValueError:
            raise ValueError("Ambos valores deben ser números enteros válidos.")
    
    def suma (self):
        return self.valor1 + self.valor2
    
    def resta (self):
        return self.valor1 - self.valor2
    
    def multiplicacion (self):
        return self.valor1 * self.valor2
    
    def division(self):
        if self.valor2 == 0:
            return "Error: No se puede dividir por cero."
        # Asumimos que valor1 y valor2 son números gracias a __init__
        return self.valor1 / self.valor2
    
    def __str__ (self):
        suma_res = self.suma()
        resta_res = self.resta()
        multiplicacion_res = self.multiplicacion()
        division_res = self.division()
        
        return (f"Resultados para los valores {self.valor1} y {self.valor2}:\n"
                f"Suma: {suma_res}\n"
                f"Resta: {resta_res}\n"
                f"Multiplicación: {multiplicacion_res}\n"
                f"División: {division_res}")

if __name__ == "__main__":
    try:
        val1_input = input("Ingrese el primer valor entero: ")
        val2_input = input("Ingrese el segundo valor entero: ")
        calculadora_obj = Calculadora(val1_input, val2_input)
        print(calculadora_obj)

    except ValueError as ve:
        print(f"Error de entrada: {ve}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")




