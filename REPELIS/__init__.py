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

@app.route("/actores")
def genero():
    consulta = """
SELECT first_name, last_name from actor
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_actores = res.fetchall()
    pagina = render_template('actores.html',
                             actores = lista_actores)
    return pagina