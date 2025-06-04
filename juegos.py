#Ejercicio juegos

import random as r

print("Bienvenido/a. Hoy jugaremos con números y la suerte. Te sientes listo?")

num= r.randint(1,5)

usernum= input("Solo necesito que me digas un número del 1 al 5, veremos si adivinas lo que estoy pensando ;) ")
usnum= int(usernum)

if usnum==num:
    print("Felicidades, has ganado! Eres muy bueno en esto :D")
else:
    print(f"Lo siento, el número que estaba pensando era: {num}, intenta nuevamente")

