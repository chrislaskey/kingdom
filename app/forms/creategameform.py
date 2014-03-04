from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import TextField, SelectField, SubmitField 


class CreateGameForm(Form):
    game_name = TextField(u'Game Name', validators=[DataRequired()])
    game_type = SelectField(
        u'Game Type',
        choices=[(u'', u''), (u'classic', u'Classic')],
        validators=[DataRequired()]
    )
    submit = SubmitField(u'Create Game')
