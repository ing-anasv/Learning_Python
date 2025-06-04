# Ejemplo completo de Programación Orientada a Objetos en Python
# Sistema de gestión de empleados de una empresa

from abc import ABC, abstractmethod
from datetime import datetime

# Clase base abstracta (Abstracción)
class Persona(ABC):
    """Clase abstracta que representa a una persona"""
    
    def __init__(self, nombre, edad, identificacion):
        self._nombre = nombre  # Atributo protegido (Encapsulación)
        self._edad = edad
        self.__identificacion = identificacion  # Atributo privado (Encapsulación)
    
    # Métodos getter y setter (Encapsulación)
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío")
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def identificacion(self):
        return self.__identificacion
    
    # Método abstracto que debe ser implementado por las clases hijas
    @abstractmethod
    def obtener_info(self):
        pass
    
    def saludar(self):
        return f"Hola, soy {self._nombre}"

# Clase hija que hereda de Persona (Herencia)
class Empleado(Persona):
    """Clase que representa a un empleado"""
    
    contador_empleados = 0  # Atributo de clase
    
    def __init__(self, nombre, edad, identificacion, puesto, salario):
        super().__init__(nombre, edad, identificacion)  # Llamada al constructor padre
        self.puesto = puesto
        self._salario = salario
        self.fecha_contratacion = datetime.now()
        Empleado.contador_empleados += 1
        self.id_empleado = Empleado.contador_empleados
    
    # Implementación del método abstracto (Polimorfismo)
    def obtener_info(self):
        return f"Empleado: {self._nombre}, Puesto: {self.puesto}, ID: {self.id_empleado}"
    
    def calcular_salario_anual(self):
        return self._salario * 12
    
    def aumentar_salario(self, porcentaje):
        if porcentaje > 0:
            self._salario += self._salario * (porcentaje / 100)
            return f"Salario aumentado. Nuevo salario: ${self._salario:,.2f}"
        else:
            return "El porcentaje debe ser positivo"
    
    # Sobrescritura de método (Polimorfismo)
    def saludar(self):
        return f"Hola, soy {self._nombre} y trabajo como {self.puesto}"
    
    # Método estático
    @staticmethod
    def es_salario_valido(salario):
        return salario > 0
    
    # Método de clase
    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados

# Clase hija que hereda de Empleado (Herencia multinivel)
class Gerente(Empleado):
    """Clase que representa a un gerente"""
    
    def __init__(self, nombre, edad, identificacion, salario, departamento, empleados_a_cargo=None):
        super().__init__(nombre, edad, identificacion, "Gerente", salario)
        self.departamento = departamento
        self.empleados_a_cargo = empleados_a_cargo or []
    
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.empleados_a_cargo.append(empleado)
            return f"{empleado.nombre} agregado al equipo de {self._nombre}"
        else:
            return "Solo se pueden agregar objetos de tipo Empleado"
    
    def obtener_info(self):
        info_base = super().obtener_info()
        return f"{info_base}, Departamento: {self.departamento}, Empleados a cargo: {len(self.empleados_a_cargo)}"
    
    def calcular_bono_gerencial(self):
        return self._salario * 0.15  # 15% del salario base

# Clase independiente para demostrar composición
class Proyecto:
    """Clase que representa un proyecto"""
    
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleados_asignados = []
        self.estado = "En planificación"
    
    def asignar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.empleados_asignados.append(empleado)
            return f"{empleado.nombre} asignado al proyecto {self.nombre}"
        else:
            return "Solo se pueden asignar empleados válidos"
    
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["En planificación", "En progreso", "Completado", "Cancelado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            return f"Estado del proyecto cambiado a: {nuevo_estado}"
        else:
            return f"Estado no válido. Estados disponibles: {estados_validos}"

# Función para demostrar polimorfismo
def mostrar_informacion_personas(personas):
    """Función que demuestra polimorfismo - acepta cualquier objeto que herede de Persona"""
    print("\n=== INFORMACIÓN DE PERSONAS ===")
    for persona in personas:
        print(f"- {persona.obtener_info()}")
        print(f"  Saludo: {persona.saludar()}")
        print()

# Programa principal - Demostración del sistema
def main():
    print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===\n")
    
    # Crear empleados
    empleado1 = Empleado("Ana García", 28, "12345678", "Desarrolladora", 3500)
    empleado2 = Empleado("Carlos López", 32, "87654321", "Diseñador", 3000)
    empleado3 = Empleado("María Rodríguez", 26, "11223344", "Analista", 2800)
    
    # Crear gerente
    gerente1 = Gerente("Roberto Silva", 45, "99887766", 6000, "Tecnología")
    
    # Demostrar métodos de clase y estáticos
    print(f"Total de empleados creados: {Empleado.obtener_total_empleados()}")
    print(f"¿Es válido un salario de 3500? {Empleado.es_salario_valido(3500)}")
    print()
    
    # Demostrar encapsulación
    print("=== DEMOSTRANDO ENCAPSULACIÓN ===")
    print(f"Nombre del empleado: {empleado1.nombre}")
    empleado1.nombre = "Ana García Pérez"  # Usando setter
    print(f"Nombre actualizado: {empleado1.nombre}")
    print(f"ID privado: {empleado1.identificacion}")  # Acceso a atributo privado mediante property
    print()
    
    # Demostrar herencia y polimorfismo
    personas = [empleado1, empleado2, empleado3, gerente1]
    mostrar_informacion_personas(personas)
    
    # Demostrar métodos específicos
    print("=== OPERACIONES CON EMPLEADOS ===")
    print(empleado1.aumentar_salario(10))
    print(f"Salario anual de {empleado1.nombre}: ${empleado1.calcular_salario_anual():,.2f}")
    print()
    
    # Demostrar relaciones entre objetos
    print("=== GESTIÓN DE EQUIPOS ===")
    print(gerente1.agregar_empleado(empleado1))
    print(gerente1.agregar_empleado(empleado2))
    print(gerente1.obtener_info())
    print(f"Bono gerencial: ${gerente1.calcular_bono_gerencial():,.2f}")
    print()
    
    # Demostrar composición con proyectos
    print("=== GESTIÓN DE PROYECTOS ===")
    proyecto1 = Proyecto("App Móvil", "Desarrollo de aplicación móvil para clientes")
    print(proyecto1.asignar_empleado(empleado1))
    print(proyecto1.asignar_empleado(empleado3))
    print(proyecto1.cambiar_estado("En progreso"))
    print(f"Proyecto: {proyecto1.nombre}")
    print(f"Estado: {proyecto1.estado}")
    print(f"Empleados asignados: {len(proyecto1.empleados_asignados)}")
    print()
    
    # Demostrar manejo de errores
    print("=== MANEJO DE ERRORES ===")
    try:
        empleado_invalido = Empleado("", 25, "123", "Dev", -1000)
    except ValueError as e:
        print(f"Error capturado: {e}")
    
    print("\n=== FIN DE LA DEMOSTRACIÓN ===")

# Ejecutar el programa
if __name__ == "__main__":
    main()