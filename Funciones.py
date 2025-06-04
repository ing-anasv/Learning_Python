#Prueba de funciones

def saludo(nombre):
    print(f"Hola, {nombre}")

def par(num):
    if (num/2)==0: 
        return True
    else:
        return False
    
def mean(lista):
    suma=0
    for i in range(len(lista)):
        suma= suma+lista[i]
    prom= suma/len(lista)
    return prom

lista= [1, 4, 5, 2]

saludo("Ana")

resultado=par(5)
if resultado==True:
    print("Es par")
else:
    print("Es impar")

promedio= mean(lista)
print(f"El promedio de la lista es: {promedio}")

from utils import calculadora

suma= calculadora.suma(1,2,3,4)
resta= calculadora.resta(10,5,2)
mul= mult(1,2,3,6)
div= calculadora.div(12,2,4)

print(suma)
print(resta)
print(mul)
print(div)