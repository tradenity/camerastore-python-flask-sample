from flask import render_template, request, redirect, session, abort
from camerastore import app
from camerastore.auth import login_required
from camerastore.forms import CheckoutForm, ShippingForm
from tradenity.resources import Address, Customer, Order, ShoppingCart, Country, State, ShippingMethod
from tradenity.resources import PaymentToken, CreditCardPayment
from tradenity.exceptions import EntityNotFoundException


@app.route("/orders")
@login_required
def index():
    orders = Order.find_all_by(customer=session['customer_id'])
    return render_template("orders/index.html", orders=orders)


@app.route("/orders/<order_id>")
@login_required
def show(order_id):
    try:
        order = Order.find_by_id(order_id)
        return render_template("orders/show.html", order=order)
    except EntityNotFoundException as e:
        abort(404)


@app.route("/checkout")
@login_required
def checkout():
    cart = ShoppingCart.get()
    form = CheckoutForm(obj=create_order_instance())
    populate_order_form(form)
    return render_template("orders/checkout.html", form=form, cart=cart, stripe_pub_key=app.config['STRIPE_PUBLIC_KEY'])


@app.route("/orders/create", methods=['POST'])
@login_required
def create_order():
    form = CheckoutForm(request.form)
    populate_order_form(form)
    if form.validate():
        order = construct_order(form.data)
        order.create()
        session["order_id"] = order.id
        shipping_methods = ShippingMethod.find_all_for_order(order.id)
        shipping_form = ShippingForm()
        shipping_form.shipping_method.choices = [(sm.id, sm.name) for sm in shipping_methods]
        return render_template("orders/shipping_form.html", shipping_form=shipping_form)
    else:
        print form.errors


@app.route("/orders/shipping", methods=['POST'])
@login_required
def add_shipping():
    order = Order.find_by_id(session["order_id"])
    order.shipping_method = ShippingMethod(id=request.form["shipping_method"])
    order.update()
    return render_template("orders/payment_form.html")


@app.route("/orders/payment", methods=['POST'])
@login_required
def place_order():
    order = Order.find_by_id(session["order_id"])
    payment_source = PaymentToken(token=request.form['token'], customer=Customer(id=session["customer_id"]), status="new").create()
    CreditCardPayment(order=order, payment_source=payment_source).create()
    return redirect("/orders/{id}".format(id=order.id))


@app.route("/orders/refund/<order_id>", methods=['POST'])
def refund(order_id):
    transaction = Order.refund(order_id)
    return redirect("/orders/{id}".format(id=transaction.order.id))


def create_order_instance():
    country = Country.find_one_by(iso2="US")
    order = Order()
    order.customer = Customer.find_by_id(session['customer_id'])
    order.billing_address = create_address(country)
    order.shipping_address = create_address(country)
    return order


def populate_order_form(form):
    usa = Country.find_one_by(iso2="US")
    countries = Country.find_all(size=250, sort="name")
    states = State.find_all_by(country=usa.id, size=60, sort="name")
    form.billing_address.state.choices = [(s.id, s.name) for s in states]
    form.billing_address.country.choices = [(c.id, c.name) for c in countries]
    form.shipping_address.state.choices = [(s.id, s.name) for s in states]
    form.shipping_address.country.choices = [(c.id, c.name) for c in countries]


def create_address(country):
    return Address(street_line1="3290 Hermosillo Place", street_line2="", city="Washington", state=State(),
                   zip_code="20521-3290", country=country)


def construct_order(data):
    order = Order(**data)
    order.customer = Customer(id=session["customer_id"])
    order.shipping_address = Address(**data["shipping_address"])
    order.shipping_address.state = Country(id=data["shipping_address"]["state"])
    order.shipping_address.country = Country(id=data["shipping_address"]["country"])
    order.billing_address = Address(**data["billing_address"])
    order.billing_address.state = Country(id=data["billing_address"]["state"])
    order.billing_address.country = Country(id=data["billing_address"]["country"])
    return order
