#TÉCNICA DE POLIMORFISMO
# Se presentan objetos de diferentes clases (Estudiante, Profesor) responden a la misma llamada de método ('presentarse') de la forma que les corresponde.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        # Esta parte añade un identificador para que la respuesta sea diferente
        print(f"Soy una Persona. Mi nombre es {self.nombre}.")

class Estudiante(Persona):
    def presentarse(self): # Se sobrescribe el método del padre
        print(f"Soy un Estudiante. Me llamo {self.nombre} y estoy en la universidad.")

class Profesor(Persona):
    def presentarse(self): # Sobrescribimos el método del padre
        print(f"Soy un Profesor. Mi nombre es {self.nombre} y enseño en la universidad.")

# A partir de estas lineas se presenta la función polimórfica
def realizar_presentacion_formal(persona):
    print("Inicio de presentación:")
    persona.presentarse() # Esta en específico es la llamada polimórfica
    print("Fin de presentación\n")

#Se crea y se da uso de los objetos
laura = Profesor("Laura", 35)
carlos = Estudiante("Carlos", 20)

# Se llama a la misma función con objetos de tipos diferentes
realizar_presentacion_formal(laura)
realizar_presentacion_formal(carlos)