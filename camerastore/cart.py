from flask import render_template, request, jsonify
from camerastore import app

from tradenity.resources import *


@app.route("/cart")
def view_cart():
    cart = ShoppingCart.get()
    return render_template("cart.html", cart=cart)


@app.route("/cart/add", methods=['POST'])
def add_to_cart():
    print "Product ID: ", request.form['product']
    cart = ShoppingCart.add_item(LineItem(product=Product(id=request.form['product']), quantity=int(request.form['quantity'])))
    return jsonify(cart.to_dict())


@app.route("/cart/remove/<item_id>", methods=['POST'])
def remove_from_cart(item_id):
    cart = ShoppingCart.remove(item_id)
    return jsonify(cart.to_dict())
