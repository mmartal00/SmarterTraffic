from flask import Flask, app, render_template, Blueprint, request, json
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('login.html')

@app.route('/form', methods=('GET', 'POST'))
def button_clicked():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print (username, password)
        return render_template('principal.html')
        #Tipo Usuario: 1 Jefe, 2 Eempleado
        
        tipoUsuario = 1
        

@app.route('/form1', methods=('GET', 'POST'))
def button_clicked_register():
    if request.method == 'POST':
        username = request.form['username']
        nombre = request.form['nombre']
        tipoUsuario = request.form['tipoUsusario']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        print (username, nombre, tipoUsuario, password, confirmpassword)
        return render_template('principal.html', tipoUsuario=tipoUsuario)
        """"
        if (tipoUsuario == 1):
            return render_template('principal.html', tipoUsuario=tipoUsuario)
        else:
            return render_template('principal.html', tipoUsuario=tipoUsuario)
        """"

@app.route("/tablas")
def indext():
    return render_template('tables.html')


@app.route("/vista")
def indexv():
    return render_template('layout-sidenav-light.html')

@app.route("/registrar")
def indexr():
    return render_template('register.html')    

@app.route("/inicio")
def indexi():
    return render_template('principal.html')

@app.route("/recuperar")
def indexp():
    return render_template('password.html')