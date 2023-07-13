from flask import render_template, redirect, session, request, flash
from app.models.favoritos import Favorito
from app.models.usuarios import Usuario
from app.models.pizzas import Pizza
from app.models.pedidos import Pedido
from app import app


# Ruta para procesar el formulario de la pizza y mostrar los detalles en "account"
@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        Pizza.get_all(request.form)

    return render_template('recetas/detalle.html')


# Ruta para mostrar los detalles de la pizza en "account"
# @app.route('/account/<pizza_detalle>', methods=['GET'])
# def show_pizza_details(pizza_detalle):
    # Parsear los detalles de la pizza desde la URL que fueron pasados como argumento
    #pizza_detalle = eval(pizza_detalle)

    # return render_template('detalle.html', pizza=pizza_detalle)
