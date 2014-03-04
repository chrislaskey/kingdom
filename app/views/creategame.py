from flask import flash, redirect, render_template
from flask.ext.security import login_required
from .. import app
from .. forms.creategameform import CreateGameForm


@app.route('/create-game', methods=('GET', 'POST'))
@login_required
def create_game():
    form = CreateGameForm()
    if form.validate_on_submit():
        flash(u'Successfully created new game', 'success')
        return redirect('/')
    return render_template('create-game.html', create_game_form=form)
