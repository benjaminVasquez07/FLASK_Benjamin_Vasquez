from flask import Blueprint, render_template
from . import db

bp = Blueprint('lenguaje',__name__, url_prefix="/lenguaje")

@bp.route('/')
def lenguajes():
    consulta = """
        SELEC first_name, last_name, lenguaje_id FROM lenguajes
        ORDER BY first_name, last_name ASC
    """

    con = db.get_db()
    res = con.Execute(consulta)
    lista_lenguaje = res.fetchall()
    paginalenguajes = render_template('lenguaje.html',
                                lenguaje=lista_lenguaje)
    return paginalenguajes

@bp.route('/<int:id>')
def lenguajes(id):
    consulta = """
    SELEC name, lenguaje_id from language
   WHERE language_id = ?;
    """

    con = db.get()
    res = con.execute(consulta,(id))
    lenguaje = res.fetchone()
    consulta2 = """

    """

    res = con.execute(consulta2,(id))
    lista_peliculas = res.fetchall()
    pagina = render_template('detalle_lenguaje.html',
                            lenguaje=lenguaje,
                            peliculas=lista_peliculas)

    return pagina
