#Script de práctica #2

print("Bienvenido/a a Python! Es un placer tenerte aquí.")

edad= input("Por favor ingresa tu edad: ")

edadint= int(edad)

#Comprobación de edad

if edadint < 12: 
    print("Eres un niño")

elif (edadint>12 and edadint<17):
    print("Eres adolescente")

else:
    print("Eres mayor de edad")