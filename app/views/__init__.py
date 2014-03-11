from flask import render_template
from flask.ext.security import login_required, current_user
from .. import app
from .. models import db
from .. models.games import Game
from .. models.users import User


@app.route('/')
@login_required
def index():
    return render_template(
        'index.html',
        current_user = current_user,
        is_first_login = is_first_login(),
        games = get_games()
    )


def get_games():
    return db.session.query(Game)\
        .filter(Game.players.contains(current_user)).all()


def is_first_login():
    return current_user.last_login_at == current_user.current_login_at


from . import creategame
