from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.router ("Benja")
def benja():
    return 'hala madrid!'

def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app