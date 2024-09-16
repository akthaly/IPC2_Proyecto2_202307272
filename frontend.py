from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reportes')
def reports():
    return render_template('reportes.html')

@app.route('/acerca-de')
def about():
    return render_template('about.html')

@app.route('/informacion')
def info():
    return render_template('informacion.html')

@app.route('/documentacion')
def documentation():
    return render_template('documentacion.html')

# Manejador para errores 404
@app.errorhandler(404)
def page_not_found(e):
    # Renderiza la plantilla 404.html cuando ocurre el error
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)