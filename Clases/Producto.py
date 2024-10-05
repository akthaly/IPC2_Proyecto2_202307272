from Clases.ColaInstrucciones import ColaInstrucciones

class Producto:
    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion
        self.cola_instrucciones = ColaInstrucciones()

    def cargar_instrucciones(self, instrucciones):
        instrucciones_lista = instrucciones.strip().split()
        for instruccion in instrucciones_lista:
            self.cola_instrucciones.encolar(instruccion)
            print(f"Instrucción encolada: {instruccion}")

    def obtener_siguiente_instruccion(self):
        return self.cola_instrucciones.desencolar()

    def tiene_instrucciones_pendientes(self):
        return not self.cola_instrucciones.esta_vacia()
    
    def mostrar_instrucciones(self):
        print(f"Instrucciones para {self.nombre}:")
        self.cola_instrucciones.mostrar()

    def __str__(self):
        return f"Nombre producto: {self.nombre}, Elaboración: {self.elaboracion}"