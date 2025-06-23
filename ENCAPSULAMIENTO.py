# TÉCNICA DE ENCAPSULAMIENTO
# Se debe considerar que la clase "Carro" encapsula los datos y métodos.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__combustible = 0  

    # Se expone un método público para cargar combustible. Esta es la forma correcta en la que se debe modificar el estado.
    def cargar_combustible(self, litros):
        if litros > 0:
            self.__combustible += litros
            print(f"Se cargaron {litros} litros. Tanque actual: {self.__combustible} L")
        else:
            print("La cantidad de litros debe ser positiva.")

    # Este bloque es el método que sirve para consultar el estado del combustible.
    def consultar_combustible(self):
        print(f"El carro {self.marca} {self.modelo} tiene {self.__combustible} L de combustible.")

#Se crea y se da uso del objeto
mi_carro = Carro("Toyota", "Corolla")

# Se usan los métodos públicos para interactuen con el objeto
mi_carro.consultar_combustible()
mi_carro.cargar_combustible(20)

try:
    mi_carro.__combustible = 100
    print("Se modificó el combustible directamente.")
except AttributeError as e:
    print(f"\nError: No se puede acceder a '__combustible'. {e}")

# La forma correcta de ver el estado es a través de su método correspondiente
print("\nComprobando el estado final:")
mi_carro.consultar_combustible()