import functools

from flask import render_template, Blueprint

bp = Blueprint('orgadm', __name__, url_prefix='/orgadm')

@bp.route('/')
def index():
    return render_template('orgadm/index.html')

