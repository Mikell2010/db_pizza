from flask import render_template, redirect, session, request, flash
from app.models.favoritos import Favorito
from app.models.usuarios import Usuario
from app.models.pizzas import Pizza
from app.models.pedidos import Pedido
from app import app


@app.route('/menu_principal')
def menu_principal():

    if 'usuario' not in session:
        return redirect('/login')

    pizzas = Pizza.get_all()
    favoritos = Favorito.get_all()

    nombre_favoritos = []

    for i in favoritos:
        if (i["usuario_id"] == session["usuario"]["usuario_id"]):
            nombre_favoritos.append(Pizza.get(i["pizza_id"]))

    return render_template('recetas/inicio.html', favoritos=nombre_favoritos, pizzas=pizzas)


@app.route('/agregar_pizza', methods=['POST'])
def agregar_pizza():
    print("POST: ", request.form)

    if not Pizza.validar(request.form):
        return redirect('/menu_principal')

    Pizza.agregar(request.form)

    return redirect('/menu_principal')


@app.route('/procesar_pizza', methods=['POST'])
def procesar_pizza():
    print("POST: ", request.form)

    data = {
        **request.form,
        "usuario_id": session['usuario']['usuario_id']
    }
    pizza = Pizza.save(data)

    flash(f"Pizza {pizza.nombre} creada exitosamente", "success")
    return redirect("/menu_principal")


@app.route('/eliminar_pizza/<int:id>')
def eliminar_pizza(id):
    Pizza.delete(id)
    return redirect("/menu_principal")


@app.route('/editar_pizza/<int:id>')
def editar_pizza(id):
    pizza = Pizza.get_by_id(id)
    # pendiente logica y template
    return render_template('recetas/crear.html', pizza=pizza)


@app.route('/actualizar_pizza', methods=['POST'])
def actualizar_pizza():
    print("POST: ", request.form)

    if not Pizza.validar(request.form):
        return redirect('/menu_principal')

    Pizza.actualizar(request.form)

    return redirect('/menu_principal')


@app.route('/agregar_favorito', methods=['POST'])
def agregar_favorito():
    print("POST: ", request.form)

    if not Favorito.validar(request.form):
        return redirect('/menu_principal')

    Favorito.agregar(request.form)

    return redirect('/menu_principal')


# @app.route('/procesar_favorito', methods=['POST'])
# def procesar_favorito():
    print("POST: ", request.form)

    data = {
        **request.form,
        "usuario_id": session['usuario']['usuario_id']
    }
    favorito = Favorito.save(data)

    flash(f"Favorito {favorito.nombre} creado exitosamente", "success")
    return redirect("/menu_principal")


# @app.route('/editar_favorito/<int:id>')
# def editar_favorito(id):
    favorito = Favorito.get_by_id(id)
    # pendiente logica y template
    return render_template('recetas/crear.html', favorito=favorito)


@app.route('/favoritas/<int:usuario_id>')
def mostrar_pizzas_favoritas(usuario_id):
    pizzas_favoritas = Pizza.query.filter_by(favorito=True).all()
    pizzas_usuario = []

    for pizza in pizzas_favoritas:
        if pizza.usuario_id == usuario_id:
            pizzas_usuario.append(pizza)

    return render_template('favoritas.html', pizzas=pizzas_usuario)


@app.route('/actualizar_favorito', methods=['POST'])
def actualizar_favorito():
    print("POST: ", request.form)

    if not Favorito.validar(request.form):
        return redirect('/menu_principal')

    Favorito.actualizar(request.form)

    return redirect('/menu_principal')


@app.route('/sorprendeme', methods=['POST'])
def sorprendeme():
    print("POST: ", request.form)

    if not Pizza.validar(request.form):
        return redirect('/menu_principal')

    Pizza.agregar(request.form)

    return redirect('/menu_principal')


@app.route('/craft_a_pizza', methods=['GET', 'POST'])
def craft_a_pizza():
    print("POST craft_a_pizza: ", request)
    print(request.method)
    pizzas = []
    pizza_topping = []
    favorite = []

    # if request.method == 'GET':
    #     selected_toppings = request.form
    #     print(selected_toppings)
    #     total = 0

    #     for topping in selected_toppings:
    #         total += int(topping)

    if request.args.get('random') == 'true':
        pizzas = Pizza.get_random()
        pizza_topping = pizzas['descripcion_pizza']

    if request.args.get('favorite') == 'true':
        usuario_id = session['usuario']['usuario_id']
        favorite = Favorito.get_by_usuario_id(usuario_id)

        if len(favorite) > 0:
            favorite = favorite[0]
        favorite_toppings = Pizza.get(favorite['pizza_id'])
        favorite_toppings = favorite_toppings["descripcion_pizza"]

        if (len(favorite_toppings) > 0):
            pizza_topping = favorite_toppings

    return render_template(
        'recetas/crear.html',
        pizzas=pizzas,  # de la base de datos
        toppings=pizza_topping,
        favorite=favorite  # reemplazar favorite=favorite por favorite=favorite_toppings #si lo comento me funciona el random
    )


#como sumar los toppings de la pizza
#create a list of toppings
#create loop through the list and add the price of each topping to a total
#return the total make a function that does this
#call the function in the route how?
#make sure the route is a post route
#return the total in the route
#make sure the route is a post route
#make sure the form is a post form





