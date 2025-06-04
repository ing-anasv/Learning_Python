#Ejercicio archivos 

with open("/home/anasv/prueba/pruebapython/frutas.txt", "w") as f:
    f.write("Manzana\n")
    f.write("Pera\nMora")

with open("/home/anasv/prueba/pruebapython/frutas.txt", "a") as f:
    f.write("\nPapaya")

with open("/home/anasv/prueba/pruebapython/frutas.txt", "r") as f:
    for line in f:
        print(line.strip())