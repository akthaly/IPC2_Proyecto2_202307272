from Clases.Nodo import Nodo

class ListaMaquinas:
    def __init__(self):
        self.cabeza = None

    def agregar(self, maquina):
        nuevo_nodo = Nodo(maquina)
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
            actual.dato.mostrar()  # Llama al método mostrar de Maquina
            actual = actual.siguiente  # Avanzamos al siguiente nodo

    def buscar(self, nombre_maquina):
        actual = self.cabeza
        while actual is not None:
            if actual.dato.nombre == nombre_maquina:
                return actual.dato
            actual = actual.siguiente
        return None  # No encontrada

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
