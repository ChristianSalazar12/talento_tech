# Description: A simple calculator that performs basic arithmetic 
# operations and uses the match-case statement.
# author: Ing Christian Salazar

print("Calculadora")
print("Operaciones disponibles:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (x)")
print("4. División (/)")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (add, subtract, multiply, divide): ")

match operacion:
    case "add" | "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    case "subtract" | "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    case "multiply" | "x":
        resultado = num1 * num2
        print(f"{num1} x {num2} = {resultado}")
    case "divide" | "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("No se puede dividir por cero")
    case _:
        print("Operación no válida")
