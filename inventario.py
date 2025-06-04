import csv

with open("/home/anasv/prueba/pruebapython/inventario.csv", mode='w', newline= '') as file: 
    escribir= csv.writer(file)

    #Escribir fila de encabezados
    escribir.writerow(['Nombre', 'Precio', 'Stock'])

    #Pedir datos
    for i in range(3):
        print(f"\nProducto {i+1}: ")
        nombre=input("Nombre del producto: ")
        precio= input("Precio: ")
        stock= input("Cantidad en stock: ")

        #Escribir en el archivo
        escribir.writerow([nombre, precio, stock])

with open ("/home/anasv/prueba/pruebapython/inventario.csv", mode='r', newline= '') as file:
    leer= csv.reader(file)

    #Leer y mostrar encabezados
    encabezados= next(leer)
    print(f"Inventario (Columnas: {', '.join(encabezados)})")

    #Leer y mostrar filas
    for fila in leer:
        nombre, precio, stock=fila
        print(f"Producto: {nombre} | Precio: {precio} | Stock: {stock}")