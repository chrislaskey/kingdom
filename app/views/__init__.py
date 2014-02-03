from flask import render_template
from flask.ext.security import login_required
from .. import app
from .. import security


@app.route('/')
@login_required
def index():
    return render_template("index.html")
