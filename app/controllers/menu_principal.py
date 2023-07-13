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

    favoritos = Favorito.get_all()
    pizzas = Pizza.get_all()

    return render_template('recetas/inicio.html', favoritos=favoritos, pizzas=pizzas
                           )


# @app.route('/agregar_pizza', methods=['POST'])
# def agregar_pizza():
    print("POST: ", request.form)

    if not Pizza.validar(request.form):
        return redirect('/menu_principal')

    Pizza.agregar(request.form)

    return redirect('/menu_principal')

# @app.route('/procesar_pizza', methods=['POST'])
# def procesar_pizza():
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

# @app.route('/actualizar_pizza', methods=['POST'])
# def actualizar_pizza():
    print("POST: ", request.form)

    if not Pizza.validar(request.form):
        return redirect('/menu_principal')

    Pizza.actualizar(request.form)

    return redirect('/menu_principal')


# @app.route('/agregar_favorito', methods=['POST'])
# def agregar_favorito():
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


@app.route('/editar_favorito/<int:id>')
def editar_favorito(id):
    favorito = Favorito.get_by_id(id)
    # pendiente logica y template
    return render_template('recetas/crear.html', favorito=favorito)

# @app.route('/actualizar_favorito', methods=['POST'])
# def actualizar_favorito():
    print("POST: ", request.form)

    if not Favorito.validar(request.form):
        return redirect('/menu_principal')

    Favorito.actualizar(request.form)

    return redirect('/menu_principal')


# @app.route('/sorprendeme', methods=['POST'])
# def sorprendeme():
    print("POST: ", request.form)

    if not Pizza.validar(request.form):
        return redirect('/menu_principal')

    Pizza.agregar(request.form)

    return redirect('/menu_principal')


@app.route('/craft_a_pizza', methods=['GET', 'POST'])
def craft_a_pizza():
    print("POST: ", request.url)
    pizzas = []
    pizza_topping = []
    # if not Pizza.validar(request.form):
    # return redirect('/menu_principal')
    if request.method == 'post':
        Pizza.agregar(request.form)  # logica formulario

    # if (cond): si el llamaddo viene de surpriseme
    if request.args.get('random') == 'true':
        pizzas = Pizza.get_random()
        # <!-- obtener id de pizza -->
        pizza_id = pizzas['id']
        pizza_topping = pizzas['descripcion_pizza']
        print(pizza_topping)
    # toppings = pizza_topping.split('y')
    # all_pizza_toppings = Pedido.get_all_toppings(pizza_id)
    # print(all_pizza_toppings)

    return render_template(
        'recetas/crear.html',
        pizzas=pizzas,  # de la base de datos
        toppings=pizza_topping
    )

# <!-- obtener topping de la pizza -->
# <!-- marcar los checkboxs de la pizza con javascript
#     for (let i=0; i < document.f1.elements.length; i++) {
#         if(document.f1.elements[i].type === "checkbox") {
#             document.f1.elements[i].checked = true;
#         }
#     }
# -->
