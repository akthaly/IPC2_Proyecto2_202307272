from Clases.NodoColaInstrucciones import NodoInstruccion

class ColaInstrucciones:
    def __init__(self):
        self.frente = None
        self.final = None
    
    def encolar(self, dato):
        nuevo_nodo = NodoInstruccion(dato)
        if self.final is None:  # La cola está vacía
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
    
    def desencolar(self):
        if self.frente is None:  # La cola está vacía
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def mostrar(self):
        actual = self.frente
        while actual:
            print(f"Instrucción: {actual.dato}")
            actual = actual.siguiente

    def esta_vacia(self):
        return self.frente is None