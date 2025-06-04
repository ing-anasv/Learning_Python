#Prueba con ciclos

print("Bienvenido al código para practicar :D")

contador=10

print("Primero vamos a contar del 10 al 1: \n")

while contador >=1: 
    print(contador)
    contador=contador-1

print("\nAhora vamos a ver frutas: \n")

frutas= ["manzana", "pera", "piña"]

for i in range(len(frutas)):
    print(frutas[i])