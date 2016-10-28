from functools import wraps
from flask import g, request, redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'customer_id' not in session:
            session['target_url'] = request.url
            return redirect('login')
        return f(*args, **kwargs)
    return decorated_function