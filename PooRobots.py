#poo robots

#-----------------Creación de clase padre---------------------------------
class Robot:
    def __init__(self, name, energy):
        self.nombre=name
        self.energia= energy #Valor entre 0 y 100 como un porcentaje de batería

    def recargar(self):
        self.energia=100
        print(f"{self.nombre} se ha recargado completamente.")

    def accion(self):
        print(f"El robot realiza acciones genéricas :D.")

#--------------------------Creación de clases hijas------------------------------------

#Clase 1: Robot Explorador
class Explorer(Robot):
    def __init__(self, name, energy, land):
        super().__init__(name, energy) 
        self.terreno=land

    def accion(self):
        if self.energia>=30:
            print(f"{self.nombre} se dispone a explorar el terreno {self.terreno}. ")
            self.energia-=30
        else:
            print(f"{self.nombre} no tiene batería suficiente para explorar, por favor cargue el robot.")


#Clase 2: Robot Doméstico
class Houser(Robot):

    def accion(self):
        if self.energia>=20:
            print(f"{self.nombre} comenzará el proceso de limpieza. ")
            self.energia-=20

        else:
            print(f"{self.nombre} no tiene energía suficiente. Por favor cargue el robot e intente nuevamente. ")


#Clase 3: Robot Chef
class Chef(Robot):
    def __init__(self, name, energy, especialidad):
        super().__init__(name, energy)
        self._especialidad=especialidad #Convierte el atributo en uno protegido

    def accion(self):
        if self.energia>=25:
            print(f"{self.nombre} cocinará la especialidad: {self._especialidad}.")
            self.energia-=25
        else:
            print(f"{self.nombre} está muy cansado para cocinar. Energía actual: {self.energia}. ")
    
    def cambiarcomida(self,newfood):
        if newfood: 
            self._especialidad=newfood #también lo vuelve protegido
            print(f"{self.nombre} ha cambiado su especialidad a: {self._especialidad}")
        else:
            print("No puede estar vacía")

    #Función getter  para acceder a un atributo interno del objeto
    def obtenerfood(self):
        return self._especialidad

#---------------------------------Creación de Objetos y pruebas--------------------

R1= Explorer("Terreneitor", 100, "montaña")
R2= Houser("Esperancito", 15)
R3= Chef("Remy", 40, "italiana")

#Visualización primer robot
print(f"Analicemos a {R1.nombre}\n")
R1.accion()
R1.estado = R1.energia
print(f"Energía restante: {R1.estado}")
print(f"\n--------------------------------")

#Visualización del segundo robot
print(f"Ahora analicemos a {R2.nombre}\n")
R2.accion()
R2.recargar()
R2.accion()
print(f"\n--------------------------------")

#Visualización del tercer robot
print(f"Ahora analicemos a {R3.nombre}\n")
R3.accion()
print(f"Energía restante: {R3.energia}")
R3.accion()
R3.recargar()
R3.accion()
R3.cambiarcomida("Colombiana")
R3.accion()

#Forma segura de acceder a la especialidad al convertirlo en protegido
print(R3.obtenerfood())

print(f"\n--------------------------------")
