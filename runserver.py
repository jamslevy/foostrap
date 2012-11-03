import envparse

from myapp import app, init_app

env = envparse.Env(PORT=(int, 5000))


if __name__ == "__main__":
    init_app(app)
    app.run(host='0.0.0.0', port=env('PORT'))
