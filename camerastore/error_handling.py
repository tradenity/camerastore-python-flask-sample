from flask import redirect
from flask import render_template
from camerastore import app
from tradenity import Configuration
from tradenity.exceptions import SessionExpiredException


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(SessionExpiredException)
def session_expired(ex):
    Configuration.AUTH_TOKEN_HOLDER.reset()
    return redirect("/")
