import envparse
import flask
import flask_debugtoolbar
import flask_sslify


# Read in configuration from environment variables
env = envparse.Env(
    DEBUG=(bool, False),
    DEBUG_TB_INTERCEPT_REDIRECTS=(bool, False),
    REDIRECT_TO_SSL=(bool, False),
    SESSION_SECRET_KEY=str
)


app = flask.Flask(__name__)


def init_app(app):
    app.debug = env('DEBUG')
    app.secret_key = env('SESSION_SECRET_KEY')
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = env(
            'DEBUG_TB_INTERCEPT_REDIRECTS')

    # NOTE: SSLify won't redirect if DEBUG=True, so this flag just allows us
    # to turn on/off redirection in production.
    if env('REDIRECT_TO_SSL'):
        flask_sslify.SSLify(app)

    flask_debugtoolbar.DebugToolbarExtension(app)


# NOTE: These imports should remain at the bottom of this file so that when
# the models and views are imported, this module has been fully configured.
from myapp import models, views
