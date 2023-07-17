from flask import render_template, redirect, session, request, flash, url_for
from app.models.favoritos import Favorito
from app.models.usuarios import Usuario
from app.models.pizzas import Pizza
from app.models.pedidos import Pedido
from app import app


# Ruta para procesar el formulario de la pizza y mostrar los detalles en "account"
@app.route('/account', methods=['GET', 'POST'])
def account():
    print("account")
    if request.method == 'POST':
        Pizza.get_all(request.form)

    return render_template('recetas/order.html')

# Ruta para mostrar la página principal y el carrito de compras
@app.route('/carrito/')
def mostrar_carrito():
    print("carrito")
    print(session["carrito"])

    if session is None:
        session["carrito"] = {
            "id": session["usuario"]["usuario_id"],
            "productos": [
                {
                    "producto_id": 1,
                    "cantidad": 1,
                    "precio": 1000
                },
                {
                    "producto_id": 2,
                    "cantidad": 1,
                    "precio": 200
                }
            ]
        }
        session['carrito'] = []
    else:
        print("Session Found!")
        session["carrito"] = {
            "id": session["usuario"]["usuario_id"],
            "productos": [
                {
                    "producto_id": 1,
                    "cantidad": 1,
                    "precio": 1000000000000000
                },
                {
                    "producto_id": 2,
                    "cantidad": 1,
                    "precio": 200
                }
            ]
        }
        # session['carrito'] = []
    # Obtener el carrito de la sesión o crear uno nuevo

    carrito = session['carrito']
    print(session)
    # session['usuario'].append(session['usuario']['usuario_id']) sesion usuario nueva clave, agregar otra clave a la sesion
    return render_template('recetas/carrito.html', carrito=carrito)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_al_carrito():
    producto = request.form.get('producto')

    # Agregar el producto al carrito en la sesión
    session['carrito'].append(producto)

    return redirect(url_for('mostrar_carrito'))

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        Pizza.get_all(request.form)

    return render_template('recetas/detalle.html', session=session)
