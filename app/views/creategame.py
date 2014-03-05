from datetime import datetime
from flask import redirect, render_template
from flask.ext.security import login_required
from .. import app
from .. models import db
from .. models.db_helpers import db_add
from .. models.games import Game
from .. forms.creategameform import CreateGameForm


@app.route('/create-game', methods=('GET', 'POST'))
@login_required
def create_game():
    form = CreateGameForm()
    if form.validate_on_submit():
        save_create_game(form)
        return redirect('/')
    return render_template('create-game.html', create_game_form=form)


def save_create_game(form):
    new_game = Game(
        status       = 'created',
        name         = form.game_name.data,
        type         = form.game_type.data,
        description  = form.game_description.data,
        date_created = datetime.utcnow()
    )
    db_add(
        new_game,
        u'New game successfully created.',
        u'An error occured when trying to create new game.'
    )
