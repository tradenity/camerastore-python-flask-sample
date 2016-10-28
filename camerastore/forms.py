from wtforms import Form, StringField, PasswordField, FormField, validators


class CustomerForm(Form):
    firstName = StringField(u'First Name', validators=[validators.input_required()])
    lastName = StringField(u'Last Name', validators=[validators.input_required()])
    email = StringField(u'Email', validators=[validators.input_required()])


class RegistrationForm(CustomerForm):
    username = StringField(u'Username', validators=[validators.input_required()])
    password = PasswordField(u'Password', validators=[validators.input_required()])
    confirmPassword = PasswordField(u'Confirm Password', validators=[validators.input_required()])


class LoginForm(Form):
    username = StringField(u'Username', validators=[validators.input_required()])
    password = PasswordField(u'Password', validators=[validators.input_required()])


class AddressForm(Form):
    streetLine1 = StringField(u'StreetLine 1', validators=[validators.input_required()])
    streetLine2 = StringField(u'StreetLine 2')
    city = StringField(u'City', validators=[validators.input_required()])
    state = StringField(u'State', validators=[validators.input_required()])
    zipCode = StringField(u'Zip Code', validators=[validators.input_required()])
    country = StringField(u'Country', validators=[validators.input_required()])


class CheckoutForm(Form):
    customer = FormField(CustomerForm)
    billingAddress = FormField(AddressForm)
    shippingAddress = FormField(AddressForm)

