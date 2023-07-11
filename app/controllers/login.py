from flask import render_template, request, redirect, session, flash
from app.models.usuarios import Usuario
from app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route('/login')
def login():

    if 'usuario' in session:
        return redirect('/')
        

    return render_template('auth/login.html')

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    print("procesar_login")
    
    usuario_encontrado = Usuario.get_by_email(request.form['email'])
    

    if not usuario_encontrado:
        flash('Existe un error en tu correo o contraseña', 'danger')
        return redirect('/login')

    login_seguro = bcrypt.check_password_hash(usuario_encontrado.password, request.form['password'])

    data = {
        "usuario_id": usuario_encontrado.id,
        "nombre": usuario_encontrado.nombre,
        "apellido": usuario_encontrado.apellido,
        "email": usuario_encontrado.email,
        "direccion": usuario_encontrado.direccion,
        "ciudad": usuario_encontrado.ciudad,
        "region": usuario_encontrado.region,
    }

    if login_seguro:
        session['usuario'] = data
        flash('Genial, pudiste entrar sin problemas!!!!', 'success')

    else:
        flash('Existe un error en tu correo o contraseña', 'danger')
        return redirect('/login')

    return redirect('/')

@app.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    print("POST: ", request.form)

    if request.form['password'] != request.form['confirm_password']:
        flash("La contraseña no es igual", "danger")
        return redirect('/login')
    
    if not Usuario.validar(request.form):
        return redirect('/login')

    password_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'email': request.form['email'],
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'password': password_hash,
        'direccion': request.form['direccion'],
        'ciudad': request.form['ciudad'],
        'region': request.form['region'],
    }

    existe_usuario = Usuario.get_by_email(request.form['email'])
    if existe_usuario:
        flash("el correo ya está registrado.", "danger")
        return redirect('/login')


    resultado = Usuario.save(data)
    if resultado:
        flash('Genial, pudiste entrar sin problemas!!!!', "success")
    else:
        flash('Existe un error en tu correo o contraseña', "danger")

    return redirect('/login')

@app.route('/salir')
def salir():
    session.clear()
    flash('Saliste sin problemas!!!', 'info')
    return redirect('/login')

