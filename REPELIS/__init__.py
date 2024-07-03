from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route ("/Benja")
def benja():
    return 'hala madrid!'

from . import actores
app.register_blueprint(actores.bp)