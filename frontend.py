from flask import Flask, render_template, request, redirect, url_for
from xml.dom import minidom
from Clases.ListaMaquinas import ListaMaquinas
from Clases.ListaProductos import ListaProductos
from Clases.Maquina import Maquina
from Clases.Producto import Producto
from Clases.Robot import ejecutar_maquina  # Cambiar por ejecutar ensamblaje directamente

app = Flask(__name__)
maquinas = ListaMaquinas()

@app.route('/')
def home():
    return render_template('open.html')

@app.route('/datos', methods=['POST'])
def analizarDatosXML():
    archivo = request.files.get('file')
    if archivo and archivo.filename != '':
        doc = minidom.parse(archivo)
        root = doc.documentElement
        
        elementosMaquina = root.getElementsByTagName('Maquina')

        for maquina in elementosMaquina:
            nombre = maquina.getElementsByTagName('NombreMaquina')[0].firstChild.data
            n = int(maquina.getElementsByTagName('CantidadLineasProduccion')[0].firstChild.data)
            m = int(maquina.getElementsByTagName('CantidadComponentes')[0].firstChild.data) + 1
            tiempoEnsamblaje = int(maquina.getElementsByTagName('TiempoEnsamblaje')[0].firstChild.data)
            productos = ListaProductos()
            
            elementosProducto = maquina.getElementsByTagName('Producto')
            for producto in elementosProducto:
                nombreProducto = producto.getElementsByTagName('nombre')[0].firstChild.data
                elaboracion = producto.getElementsByTagName('elaboracion')[0].firstChild.data
                elaboracion = ' '.join(elaboracion.split())

                objProducto = Producto(nombreProducto, elaboracion)
                objProducto.cargar_instrucciones(elaboracion)
                productos.agregar(objProducto)

            objMaquina = Maquina(nombre, n, m, tiempoEnsamblaje, productos)
            maquinas.agregar(objMaquina)
        
        maquinas.mostrar()

        # Pasamos 'enumerate' como parte del contexto de la plantilla
        return render_template('reportes.html', maquinas=maquinas, enumerate=enumerate)

    else:
        return redirect(url_for('ayuda'))
    
@app.route('/mostrar_instrucciones', methods=['POST'])
def mostrar_instrucciones():
    maquina_nombre = request.form['maquina']
    producto_nombre = request.form['producto']
    
    maquina = maquinas.buscar(maquina_nombre)
    producto = maquina.productos.buscar(producto_nombre) if maquina else None

    instrucciones = producto.elaboracion if producto else None
    
    return render_template('reportes.html', maquinas=maquinas, instrucciones=instrucciones)



@app.route('/reporte', methods=['POST'])
def seleccionar_producto():
    # Recibe los datos del formulario (máquina y producto seleccionados)
    indice_maquina = int(request.form['maquina'])
    indice_producto = int(request.form['producto'])

    maquina_seleccionada = maquinas.obtener(indice_maquina)  # Accede a la máquina seleccionada
    producto_seleccionado = maquina_seleccionada.productos.obtener(indice_producto)  # Accede al producto seleccionado

    # Ejecuta el ensamblaje del producto seleccionado en la máquina seleccionada
    ejecutar_maquina(maquina_seleccionada, producto_seleccionado)
    
    return redirect(url_for('home'))


@app.route('/reporte')
def reporte():
    return render_template('reportes.html', maquinas=maquinas, enumerate=enumerate)

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
