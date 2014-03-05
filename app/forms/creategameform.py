from flask_wtf import Form
from wtforms.validators import AnyOf, DataRequired, Optional
from wtforms import TextField, SelectField, SubmitField 


class CreateGameForm(Form):
    game_type_choices = [('', ''), ('classic', 'Classic')]
    game_type_keys = [x[0] for x in game_type_choices if x[0]]

    game_name = TextField('Game Name', validators=[DataRequired()])
    game_type = SelectField(
        'Game Type',
        choices = game_type_choices,
        validators=[DataRequired(), AnyOf(game_type_keys)]
    )
    game_description = TextField('Game Description', validators=[Optional()])
    submit = SubmitField('Create Game')
