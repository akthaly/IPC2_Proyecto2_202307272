from flask import Flask, render_template, request, redirect, url_for
from xml.dom import minidom 
from Clases.ListaMaquinas import ListaMaquinas
from Clases.ListaProductos import ListaProductos
from Clases.Maquina import Maquina
from Clases.Producto import Producto

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
            m = int(maquina.getElementsByTagName('CantidadComponentes')[0].firstChild.data)
            tiempoEnsamblaje = int(maquina.getElementsByTagName('TiempoEnsamblaje')[0].firstChild.data)
            productos = ListaProductos()
            

            elementosProducto = maquina.getElementsByTagName('Producto')
            for producto in elementosProducto:
                nombreProducto = producto.getElementsByTagName('nombre')[0].firstChild.data
                elaboracion = producto.getElementsByTagName('elaboracion')[0].firstChild.data
                elaboracion = ' '.join(elaboracion.split())

                objProducto = Producto(nombreProducto, elaboracion)
                productos.agregar(objProducto)

            objMaquina = Maquina(nombre, n, m, tiempoEnsamblaje, productos)
            maquinas.agregar(objMaquina)
        
        maquinas.mostrar()

        if archivo:
            print(f"Archivo recibido: {archivo.filename}")
            # Aquí puedes procesar el archivo, leer su contenido, etc.
        return redirect(url_for('home'))
    else :
        return redirect(url_for('ayuda'))

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)