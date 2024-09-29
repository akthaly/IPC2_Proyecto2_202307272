from Clases.Nodo import Nodo

class ListaProductos:
    def __init__(self):
        self.cabeza = None # Nodo de inicio de la lista de productos

    def agregar(self, producto):
        nuevoNodo = Nodo(producto)
        if not self.cabeza:
            self.cabeza = nuevoNodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevoNodo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:  # Recorremos mientras haya nodos
            print(actual.dato)
            actual = actual.siguiente  # Avanzamos al siguiente nodo

    