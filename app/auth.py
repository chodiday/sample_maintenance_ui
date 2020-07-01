import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#import database modules and other db tools here depends on the specs.
#from werkzeug.security import check_password_hash, generate_password_hash
#from app.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #db = get_db()
        error = None
        # user = db.execute(
        #     'SELECT * FROM user WHERE username = ?', (username,)
        # ).fetchone()

        # if user is None:
        #     error = 'Incorrect username.'
        # elif not check_password_hash(user['password'], password):
        #     error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = username #user['id']
            session['room'] = username
            return redirect(url_for('index'))

        flash(error)

    elif request.method == 'GET':
        user_id = session.get('user_id')
        if user_id != None:
            return redirect(url_for('index'))

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        # g.user = get_db().execute(
        #     'SELECT * FROM user WHERE id = ?', (user_id,)
        # ).fetchone()
        user = {'username': user_id, 'password': 'pc01'}
        g.user = user


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))