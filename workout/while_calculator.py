#add the description of the code
# This code implements a scientific calculator that allows users to perform various mathematical operations.
# The calculator supports addition, subtraction, multiplication, division, exponentiation, square root,
# logarithm base 10, and trigonometric functions (sine, cosine, tangent
# Author: Ing Christian Salazar

import math
def get_numbers(option):
    operations = {
        "1": "add",
        "2": "subtract",
        "3": "multiply",
        "4": "divide",
        "5": "power",
        "6": "sqrt",
        "7": "log10",
        "8": "sin",
        "9": "cos",
        "10": "tan"
    }

    operation = operations[option]

    if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    else:
        num1 = float(input("Ingrese el número: "))
        num2 = 0

    return num1, num2, operation

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

def power(a, b):
    return a ** b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "No se puede calcular la raíz cuadrada de un número negativo"

def log_base10(a):
    if a > 0:
        return math.log10(a)
    else:
        return "No se puede calcular el logaritmo de un número negativo o cero"

def sine(a):
    return math.sin(a)

def cosine(a):
    return math.cos(a)

def tangent(a):
    try:
        return math.tan(a)
    except ValueError:
        return "Error al calcular la tangente para este valor"

def calculate(num1, num2, operation):
    if operation == 'add':
        result = add(num1, num2)
        message = f" RESULTADO ->{num1} + {num2} = {result}"
    elif operation == 'subtract':
        result = subtract(num1, num2)
        message = f" RESULTADO ->{num1} - {num2} = {result}"
    elif operation == 'multiply':
        result = multiply(num1, num2)
        message = f" RESULTADO ->{num1} x {num2} = {result}"
    elif operation == 'divide':
        result = divide(num1, num2)
        message = f" RESULTADO ->{num1} / {num2} = {result}"
    elif operation == 'power':
        result = power(num1, num2)
        message = f" RESULTADO ->{num1} ^ {num2} = {result}"
    elif operation == 'sqrt':
        result = square_root(num1)
        message = f" RESULTADO -> La raíz cuadrada de {num1} es {result}"
    elif operation == 'log10':
        result = log_base10(num1)
        message = f" RESULTADO ->log10({num1}) = {result}"
    elif operation == 'sin':
        result = sine(num1)
        message = f" RESULTADO ->sen({num1}) = {result}"
    elif operation == 'cos':
        result = cosine(num1)
        message = f" RESULTADO ->cos({num1}) = {result}"
    elif operation == 'tan':
        result = tangent(num1)
        message = f" RESULTADO ->tan({num1}) = {result}"
    else:
        message = "Operación no válida"

    return message

def scientific_calculator():
    while True:
        print("\n======= Calculadora ==========")
        print("| Operaciones disponibles       |")
        print("|======= Calculadora ===========|")
        print("| 1. Suma (+)                   |")
        print("| 2. Resta (-)                  |")
        print("| 3. Multiplicación (x)         |")
        print("| 4. División (/)               |")
        print("| 5. Potencia (^)               |")
        print("| 6. Raíz cuadrada (sqrt)       |")
        print("| 7. Logaritmo base 10 (log10)  |")
        print("| 8. Seno (sen)                 |")
        print("| 9. Coseno (cos)               |")
        print("| 10. Tangente (tan)            |")
        print("| 0. Salir                      |")
        print("|===============================|")
        option = input("Seleccione una operación (0-10): ")

        if option == "0":
            print("Sesión terminada")
            break

        try:
            if option in [str(i) for i in range(1, 11)]:
                num1, num2, operation = get_numbers(option)
                result = calculate(num1, num2, operation)
                print(result)
            else:
                print("Opción no válida. Por favor seleccione una opción del menú (0-10).")
        except ValueError:
            print("Error: Entrada inválida. Por favor ingrese números válidos.")

        input("Presione Enter para continuar...")

# Ejecutar
scientific_calculator()
