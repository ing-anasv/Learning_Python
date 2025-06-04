#POO
"""
class Perro:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad
    
    def ladrar(self):
        print(f"{self.nombre} dice guau")

#Crear objetos
mi_perro= Perro("Abbie", 1)
mi_angel = Perro("Charly", 9)

mi_perro.ladrar()

"""

class Cafetera:
    #definir constructor
    def __init__(self, marca, capacidad):
        #Marca es un str, capacidad en mL y nivel actual que es cuanto liquido hay
        self.marca= marca
        self.capacidad= capacidad
        self.nivel= 0 #La cafetera empieza vacía

    def llenar(self): 
        #Pone el nivel actual al máximo es decir la capacidad total
        self.nivel= self.capacidad 
        print(f"La caferera {self.marca} está llena ({self.capacidad} mL).")
    
    def servir(self, tazas, size=100): #debe recibir el número de tazas a llenar
        #Resta 100mL por taza del nivel actual. Si no alcanza avisa
        if not isinstance(tazas,int) or tazas<=0:
            print("Por favor ingresa un número entero positivo de tazas.")
            return
        
        cant= tazas*size #porque son 100mL por taza
        if cant>self.nivel:
            print("No hay cantidad suficiente de café para servir esas tazas")
        else:
            self.nivel-= cant
            print(f"Se han servido {tazas} taza(s). Quedan {self.nivel} mL")

    def estado(self):
        #Imprime cuanta agua queda
        porcentaje= (self.nivel/self.capacidad)*100
        print(f"Nivel actual: {self.nivel} mL de café ({porcentaje}%).")

    def vaciar(self):
        self.nivel=0
        print("La cafetera se ha vaciado")

    def __str__(self):
        return f"Cafetera {self.marca} ({self.capacidad} ml), nivel actual: {self.nivel} mL"

#-------------------------------------------------------------------------
#Clase cafetera hija

class CafProgramable(Cafetera):
    def __init__(self, marca,capacidad,hora):
        super().__init__(marca,capacidad) #Llama al constructor de la clase padre
        self.hora= hora

    def programar(self,nueva_hora):
        self.hora=nueva_hora
        print(f"Cafetera programada para las {self.hora} hs.")

    def mostrartime(self):
        print(f"La cafetera está programada para las {self.hora}")


#---------------Imprimir---------------------------------------------------------
caf1= CafProgramable("Anita", 1000, "08:00")

print(caf1)

caf1.estado()

caf1.llenar()

caf1.programar("07:00")

caf1.mostrartime()

caf1.servir(4, 250)

caf1.estado()

caf1.vaciar()

print(caf1)