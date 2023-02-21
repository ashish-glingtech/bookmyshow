from flask import Blueprint

from .auth import HomeView

bp = Blueprint('views', __name__)


# Routes of the `Movie` Module
bp.add_url_rule('/', view_func=HomeView.as_view('index'))
