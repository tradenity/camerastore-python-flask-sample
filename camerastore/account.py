from flask import render_template, request, redirect, session, flash
from tradenity.resources import Customer
from tradenity.resources.utils import is_valid_password
from camerastore import app
from camerastore.forms import LoginForm, RegistrationForm


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("account/login.html", form=form)


@app.route("/signin", methods=['POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate():
        cust = Customer.find_one_by(username=form.username.data)
        if cust is not None and is_valid_password(cust, form.password.data):
            session['customer_id'] = cust.id
            if 'target_url' in session:
                target_url = session['target_url']
                session.pop('target_url', None)
            else:
                target_url = "/"
            return redirect(target_url)

    flash("Invalid credentials, try again!")
    return render_template("account/login.html", form=form)


@app.route("/logout")
def logout():
    del session['customer_id']
    return redirect("/")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("account/register.html", form=form)


@app.route("/account/create", methods=['POST'])
def create():
    form = RegistrationForm(request.form)
    customer = Customer()
    if request.method == 'POST' and form.validate():
        form.populate_obj(customer)
        print "CUSTOMER: ", customer
        customer.create()
        return redirect("/login")
    else:
        return render_template("account/register.html", form=form)
