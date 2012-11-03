import flask

import myapp


@myapp.app.route('/hello')
def view_hello():
    hello_msg = myapp.models.hello.get()
    return flask.render_template('hello/view.html', hello_msg=hello_msg)
