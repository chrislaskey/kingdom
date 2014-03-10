from flask import render_template
from flask.ext.security import login_required, current_user
from .. import app
from .. models import db
from .. models.games import Game
from .. models.users import User


@app.route('/')
@login_required
def index():
    games = db.session.query(Game)\
        .filter(Game.players.contains(current_user)).all()
    return render_template(
        'index.html',
        current_user = current_user,
        games = games
    )


from . import creategame
