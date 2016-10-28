import sys

from tradenity.sdk import Tradenity
from tradenity_flask.sdk.ext.auth import FlaskAuthTokenHolder
from camerastore import app


# Change this value to reflect your stripe public key.
app.config['STRIPE_PUBLIC_KEY'] = 'pk_xxxxxxxxxxxxxxxxxxxxxxx'

# Change this value to reflect your store's API key.
Tradenity.API_KEY = 'sk_xxxxxxxxxxxxxxxxx'
Tradenity.TOKEN_HOLDER = FlaskAuthTokenHolder

from camerastore import shop
from camerastore import cart
from camerastore import account
from camerastore import orders
from camerastore import error_handling

if __name__ == "__main__":
    app.run(debug=True)
