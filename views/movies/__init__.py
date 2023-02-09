from flask import Blueprint

from .movie import MoviesList
from .booking import BookingList

movie_view_bp = Blueprint('movie_view_bp', __name__)


# Routes of the `Movie` Module
movie_view_bp.add_url_rule('/movies', view_func=MoviesList.as_view('index'))
movie_view_bp.add_url_rule('/booking', view_func=BookingList.as_view('booking'))
