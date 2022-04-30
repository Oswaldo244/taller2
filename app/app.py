from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)  # vble que lanzará el aplicativo
# decorador para ruta de inicio


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/galeria', methods=['GET', 'POST'])
def galeria():

    
    datos = {
        "ciudad1":'Medellin',"ciudad2":"Cartagena","ciudad3":"Santa Marta",
        "precio1":'150000/dia',"precio2":"180000/dia","precio3":"16000/dia",
        "habitacion1":'3 habitaciones',"habitacion2":"2 habitaciones","habitacion3":"4 habitaciones",
        "direccion1":'Calle 67 #56-10', "direccion2":"Carrera 34 #23-10", "direccion3":"Calle 78 #45-37"
    }

    if request.method == 'POST':
        return redirect(url_for('index') )

    return render_template('galeria.html', data= datos)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():

    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('contacto.html')

@app.route('/nosotros', methods=['GET', 'POST'])
def nosotros():

    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('nosotros.html')


if __name__ == "__main__":
    app.run(debug=True, port=5300)
