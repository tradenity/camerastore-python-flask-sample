from flask import render_template, request, jsonify
from camerastore import app

from tradenity.sdk.entities import *


@app.route("/")
def home():
    categories = Category.find_all()
    collections = Collection.find_all()
    cart = ShoppingCart.get()
    return render_template("index.html", categories=categories, collections=collections, cart=cart)


@app.route("/products")
def products():
    print request.args
    if 'query' in request.args:
        products = Product.find_all(title=request.args['query'])
    else:
        products = Product.find_all()
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_by_name("featured")
    cart = ShoppingCart.get()
    return render_template("products.html", brands=brands, categories=categories, products=products, featured=featured, cart=cart)


@app.route("/categories/<category_id>")
def browse_category(category_id):
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_by_name("featured")
    products = Product.find_all_by_category(category_id)
    cart = ShoppingCart.get()
    return render_template("products.html", brands=brands, categories=categories, products=products, featured=featured, cart=cart)


@app.route("/brands/<brand_id>")
def browse_brand(brand_id):
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_by_name("featured")
    products = Product.find_all_by_brand(brand_id)
    cart = ShoppingCart.get()
    return render_template("products.html", brands=brands, categories=categories, products=products, featured=featured, cart=cart)


@app.route("/products/<product_id>")
def product_details(product_id):
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_by_name("featured")
    product = Product.find_by_id(product_id)
    cart = ShoppingCart.get()
    return render_template("single.html", brands=brands, categories=categories, product=product, featured=featured, cart=cart)





