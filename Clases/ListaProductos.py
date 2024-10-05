from Clases.Nodo import Nodo

class ListaProductos:
    def __init__(self):
        self.cabeza = None  # Nodo de inicio de la lista de productos

    def agregar(self, producto):
        nuevo_nodo = Nodo(producto)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:  # Recorremos mientras haya nodos
            print(actual.dato)  # Asumiendo que 'dato' tiene un método __str__ para mostrar el producto
            actual = actual.siguiente  # Avanzamos al siguiente nodo

    def obtener(self, index):
        actual = self.cabeza
        for _ in range(index):
            if actual is None:
                return None
            actual = actual.siguiente
        return actual.dato if actual else None

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato  # Devuelve el dato del nodo actual
            actual = actual.siguiente  # Avanza al siguiente nodo

    def __getitem__(self, index):
        return self.obtener(index)  # Permite la indexación