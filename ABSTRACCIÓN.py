# TÉCNICA DE ABSTRACCIÓN
# Ser presenta a clase "Biblioteca", misma que oculta la complejidad de sus operaciones

class Biblioteca:
    def __init__(self):
        # La lógica interna está oculta (abstraída) en este bloque
        self.__libros_disponibles = {"Cien años de soledad": 5, "El principito": 3}
        self.__registro_prestamos = {}

    # Este bloque representa a loos métodos privados que exponen la complejidad interna
    def __verificar_disponibilidad(self, libro):
        print(f"Paso 1: Espere un momento, estamos verificando el stock de '{libro}'...")
        return self.__libros_disponibles.get(libro, 0) > 0

    def __registrar_prestamo(self, libro, usuario):
        print(f"Paso 2: Actualizando stock y registrando préstamo para '{usuario}'...")
        self.__libros_disponibles[libro] -= 1
        self.__registro_prestamos[libro] = usuario

    def prestar_libro_a_usuario(self, libro, usuario):
        """
        Presta un libro a un usuario, ocultando todos los pasos internos.
        """
        print(f"\nIniciando proceso para prestar '{libro}' a '{usuario}'...")
        if self.__verificar_disponibilidad(libro):
            self.__registrar_prestamo(libro, usuario)
            print(f"¡Proceso completado! '{usuario}' ha retirado '{libro}'.")
        else:
            print(f"Proceso fallido. El libro '{libro}' no está disponible.")

# Se crea y se da uso al objeto
mi_biblioteca = Biblioteca()
mi_biblioteca.prestar_libro_a_usuario("Cien años de soledad", "Pedro")
mi_biblioteca.prestar_libro_a_usuario("Don Quijote", "Juan")