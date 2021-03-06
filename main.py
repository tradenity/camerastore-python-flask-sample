import sys

from tradenity import Configuration
from tradenity_flask.sdk.ext.auth import FlaskAuthTokenHolder
from camerastore import app


# Change this value to reflect your stripe public key.
app.config['STRIPE_PUBLIC_KEY'] = 'pk_xxxxxxxxxxxxxxxxxxxxxxx'

# Change this value to reflect your store's API key.
Configuration.API_KEY = 'sk_xxxxxxxxxxxxxxxxxxxxxxxxxx'
Configuration.AUTH_TOKEN_HOLDER = FlaskAuthTokenHolder()

from camerastore import shop
from camerastore import cart
from camerastore import account
from camerastore import orders
from camerastore import error_handling

if __name__ == "__main__":
    app.run(debug=True)
