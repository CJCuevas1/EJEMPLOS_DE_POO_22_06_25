# TÉCNICA DE HERENCIA ---
# Se presenta una relación "es un/a" "un Estudiante  y ES UNA Persona"

# Este bloque representa a la clase Padre 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Esta es la clase Hija 1  que hereda de estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, semestre):
        super().__init__(nombre, edad)
        self.semestre = semestre  # Este atributo es propio de un estudiante

    # Este pequeño bloque representa el método propio de estudiante
    def estudiar(self):
        print(f"{self.nombre} está estudiando para su {self.semestre} semestre.")

#Esta es la clase Hija 2 que hereda de persona
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia 

    def ensenar(self):
        print(f"{self.nombre} está enseñando la materia de {self.materia}.")

# Se crea y se da uso de los objetos
estudiante1 = Estudiante("Carlos", 20, "Segundo")
profesor1 = Profesor("Laura", 35, "Programación Orientada a Objetos")

# Cualquiera puede usar el método 'presentarse()' ya que lo heredaron de persona
print("Presentaciones")
estudiante1.presentarse()
profesor1.presentarse()

# Cada uno cuenta y usa con su propio método específico
print("\nAcciones específicas")
estudiante1.estudiar()
profesor1.ensenar()