import time
import threading

# Creamos un lock para el ensamblaje
ensamblaje_lock = threading.Lock()

# Clase para la lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class MiListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

# Función para mover el brazo robótico
def mover_brazo(num_componentes, componente_origen, componente_destino, tiempo_ensamblaje):
    if componente_destino < 0 or componente_destino >= num_componentes:
        print(f"{threading.current_thread().name}: Componente fuera de rango.")
        return

    # Movimiento desde la posición actual hasta el componente destino
    paso = 1 if componente_destino > componente_origen else -1
    print(f"Iniciando en el componente {componente_origen} en {threading.current_thread().name}...")
    
    # Guardamos el tiempo de inicio
    inicio = time.time()

    for i in range(componente_origen + paso, componente_destino + paso, paso):
        print(f"Segundo {abs(i - componente_origen)}: Moviendo al componente {i} en {threading.current_thread().name}...")
        time.sleep(1)

    print(f"{threading.current_thread().name}: Brazo robótico ha llegado al componente {componente_destino}.")
    
    # Simulación del ensamblaje
    with ensamblaje_lock:  # Solo un brazo puede ensamblar a la vez
        print(f"{threading.current_thread().name}: Empezando ensamblaje en el componente {componente_destino}...")
        for t in range(tiempo_ensamblaje):
            print(f"Segundo {componente_destino + t + 1}: Ensamblando en {threading.current_thread().name}...")
            time.sleep(1)

    # Guardamos el tiempo de fin
    fin = time.time()
    tiempo_total = fin - inicio  # Tiempo total en segundos

    print(f"{threading.current_thread().name}: Ensamblaje completado en el componente {componente_destino}.")
    print(f"{threading.current_thread().name}: Tiempo total para completar la tarea: {tiempo_total:.2f} segundos.")

# Función para ejecutar las instrucciones de un producto
def ejecutar_maquina(maquina, producto):
    print(f"Iniciando el ensamblaje para el producto: {producto.nombre} en la máquina: {maquina.nombre}")
    instrucciones = producto.cola_instrucciones
    tiempo_ensamblaje = maquina.tiempoEnsamblaje

    hilos = MiListaEnlazada()  # Usamos la lista enlazada
    posiciones_brazos = {linea: 0 for linea in range(1, maquina.n + 1)}  # Inicia en componente 0
    tiempo_total = 0  # Variable para almacenar el tiempo total
    tiempos_ensamblaje = []  # Lista para almacenar los tiempos de cada segundo

    while producto.tiene_instrucciones_pendientes():
        instruccion = producto.obtener_siguiente_instruccion()
        linea = int(instruccion[1])  # Línea de producción (Lx)
        componente_destino = int(instruccion[3])  # Componente (Cy)
        num_componentes = maquina.m  # Número de componentes de la máquina

        # Obtener la última posición del brazo para esta línea
        componente_origen = posiciones_brazos[linea]

        # Crear un hilo para mover el brazo y ensamblar
        hilo = threading.Thread(target=mover_brazo, args=(num_componentes, componente_origen, componente_destino, tiempo_ensamblaje), name=f'Brazo Robótico de la Línea {linea}')
        hilo.start()
        hilos.agregar(hilo)  # Agregar el hilo a la lista enlazada

        # Actualizar la última posición del brazo en esta línea
        posiciones_brazos[linea] = componente_destino

        # Agregar los segundos de ensamblaje a la lista
        for t in range(tiempo_ensamblaje):
            tiempos_ensamblaje.append(tiempo_total + t + 1)  # Agregar cada segundo

    # Esperar a que todos los hilos del producto actual terminen antes de pasar al siguiente
    for hilo in hilos.recorrer():  # Recorrer los hilos de la lista enlazada
        hilo.join()

    # Calcular el tiempo total en segundos
    tiempo_total += tiempo_ensamblaje * len(producto.cola_instrucciones)  # Supón que cada instrucción toma 'tiempo_ensamblaje' segundos

    return tiempo_total, tiempos_ensamblaje  # Devuelve el tiempo total y los segundos

# Nueva función para seleccionar máquina y producto
def seleccionar_maquina_y_producto(maquinas):
    print("Máquinas disponibles:")
    for index, maquina in enumerate(maquinas):  # Ahora puedes iterar sobre máquinas
        print(f"{index + 1}: {maquina.nombre}")

    seleccion_maquina = int(input("Seleccione el número de la máquina que desea usar: ")) - 1  # Convertir a índice
    maquina_seleccionada = maquinas[seleccion_maquina]  # Accede a la máquina seleccionada
    print(f"Ha seleccionado la máquina: {maquina_seleccionada.nombre}")

    # Mostrar productos de la máquina seleccionada
    print("Productos disponibles en la máquina:")
    for index, producto in enumerate(maquina_seleccionada.productos):  # Asumiendo que productos también es iterable
        print(f"{index + 1}: {producto.nombre}")

    seleccion_producto = int(input("Seleccione el número del producto que desea ensamblar: ")) - 1
    producto_seleccionado = maquina_seleccionada.productos[seleccion_producto]  # Accede al producto seleccionado

    print(f"Ha seleccionado el producto: {producto_seleccionado.nombre}")
    
    # Lógica para ensamblar el producto
    ejecutar_maquina(maquina_seleccionada, producto_seleccionado)
