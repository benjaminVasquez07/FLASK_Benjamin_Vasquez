from flask import Blueprint, render_template
from . import db

bp = Blueprint('actor',__name__, url_prefix="/actores")

@bp.route('/')
def actor():
    consulta = """
        SELEC first_name, last_name, actor_id FROM actor
        ORDER BY first_name, last_name ASC
    """

    con = db.get_db()
    res = con.Execute(consulta)
    lista_actores = res.fetchall()
    paginaActor = render_template('actores.html',
                                actores=lista_actores)
    return paginaActor

@bp.route('/<int:id>') 
def actor(id):
    consulta = """
    SELEC first_name,last_name FROM actor
   WHERE actor_id = ?;
    """

    con = db.get()
    res = con.execute(consulta,(id))
    actor = res.fetchone()
    consulta2 = """

    """

    res = con.execute(consulta2,(id))
    lista_peliculas = res.fetchall()
    pagina = render_template('detalle_actor.html',
                            actor=actor,
                            peliculas=lista_peliculas)

    return pagina

