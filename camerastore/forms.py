from wtforms import Form, StringField, PasswordField, FormField, SelectField, validators
from wtforms.compat import text_type, izip
from tradenity.resources import State, Country, ShippingMethod


class CustomerForm(Form):
    first_name = StringField(u'First Name', validators=[validators.input_required()])
    last_name = StringField(u'Last Name', validators=[validators.input_required()])
    email = StringField(u'Email', validators=[validators.input_required()])


class RegistrationForm(CustomerForm):
    username = StringField(u'Username', validators=[validators.input_required()])
    password = PasswordField(u'Password', validators=[validators.input_required()])
    confirm_password = PasswordField(u'Confirm Password', validators=[validators.input_required()])


class LoginForm(Form):
    username = StringField(u'Username', validators=[validators.input_required()])
    password = PasswordField(u'Password', validators=[validators.input_required()])


class ModelSelectField(SelectField):
    def iter_choices(self):
        for value, label in self.choices:
            if isinstance(self.data, unicode):
                yield (value, label, value == self.data)
            else:
                yield (value, label, value == self.data.id)

    def process_data(self, value):
        self.data = value


class AddressForm(Form):
    street_line1 = StringField(u'StreetLine 1', validators=[validators.input_required()])
    street_line2 = StringField(u'StreetLine 2')
    city = StringField(u'City', validators=[validators.input_required()])
    state = ModelSelectField(u'State', validators=[validators.input_required()])
    zip_code = StringField(u'Zip Code', validators=[validators.input_required()])
    country = ModelSelectField(u'Country', validators=[validators.input_required()])


class ShippingForm(Form):
    shipping_method = SelectField(u'Shipping method', validators=[validators.input_required()])


class CheckoutForm(Form):
    customer = FormField(CustomerForm)
    billing_address = FormField(AddressForm)
    shipping_address = FormField(AddressForm)

