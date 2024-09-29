
class Maquina:
    def __init__(self, nombre, n, m, tiempoEnsamblaje,  productos):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.tiempoEnsamblaje = tiempoEnsamblaje
        self.productos = productos
        

    def mostrar(self):
        print(f"Nombre Máquina: {self.nombre}, N: {self.n}, M: {self.m} Tiempo de Ensamblaje: {self.tiempoEnsamblaje}")
        print("Productos:")
        actual = self.productos.cabeza
        while actual:
            print(actual.dato)  # Usar el método __str__ de ClaseB
            actual = actual.siguiente

