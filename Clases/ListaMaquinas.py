from Clases.Nodo import Nodo

class ListaMaquinas:
    def __init__(self):
        self.cabeza = None

    def agregar(self, maquina):
        nuevoNodo = Nodo(maquina)
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
            actual.dato.mostrar()  # Llama al método mostrar de Maquina
            actual = actual.siguiente  # Avanzamos al siguiente nodo