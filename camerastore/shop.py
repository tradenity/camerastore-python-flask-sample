from flask import render_template, request, jsonify
from camerastore import app

from tradenity.resources import *


@app.route("/")
def home():
    categories = Category.find_all()
    collections = Collection.find_all()
    cart = ShoppingCart.get()
    return render_template("index.html", categories=categories, collections=collections, cart=cart)


@app.route("/products")
def products():
    if 'query' in request.args:
        products = Product.find_all_by(title=request.args['query'])
    else:
        products = Product.find_all()
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_one_by(name="featured")
    cart = ShoppingCart.get()
    return render_template("products.html", brands=brands, categories=categories, products=products, featured=featured, cart=cart)


@app.route("/categories/<category_id>")
def browse_category(category_id):
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_one_by(name="featured")
    products = Product.find_all_by(categories__contains=category_id)
    cart = ShoppingCart.get()
    return render_template("products.html", brands=brands, categories=categories, products=products, featured=featured, cart=cart)


@app.route("/brands/<brand_id>")
def browse_brand(brand_id):
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_one_by(name="featured")
    products = Product.find_all_by(brand=brand_id)
    cart = ShoppingCart.get()
    return render_template("products.html", brands=brands, categories=categories, products=products, featured=featured, cart=cart)


@app.route("/products/<product_id>")
def product_details(product_id):
    brands = Brand.find_all()
    categories = Category.find_all()
    featured = Collection.find_one_by(name="featured")
    product = Product.find_by_id(product_id)
    cart = ShoppingCart.get()
    return render_template("single.html", brands=brands, categories=categories, product=product, featured=featured, cart=cart)





