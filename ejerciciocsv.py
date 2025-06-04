import csv

datos= [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Ana', '23', 'Manizales'],
    ['Juan', '25','Cúcuta']
]

with open("/home/anasv/prueba/pruebapython/datos.csv", mode='w', newline= '') as archivo:
    escritor= csv.writer(archivo)
    escritor.writerows(datos)

with open ("/home/anasv/prueba/pruebapython/datos.csv", mode='r', newline= '') as archivo:
    lector=csv.reader(archivo)
    next(lector) #Salta la fila del encabezado
    for fila in lector:
        nombre=fila[0]
        edad=fila[1]
        ciudad=fila[2]
        print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")