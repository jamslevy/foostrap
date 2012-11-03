import flask

import myapp
from myapp.views import hello


@myapp.app.route('/')
def root():
    return flask.redirect('/hello')
