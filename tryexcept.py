#Ejercicios try except

#Validación de un número entero

"""

print("Hola, bienvenido al duplicador de números!!")

try:
    n= int(input("Solo necesito que ingreses un número entero: "))
    print(f"Excelente! El doble del número que ingresaste es: {n*2}")

except ValueError:
    print("No ingresaste un número :c")

    """

#División segura

print("Bienvenido a tu calculadora de confianza ;)")

try:
    num=float(input("Por favor ingresa el numerador: "))
    den=float(input("Por favor ingresa el denominador: "))
    print(f"El resultado de la división es: {num/den}")

except ValueError:
    print("Debes ingresar números")

except ZeroDivisionError:
    print("El denominador no puede ser cero") 