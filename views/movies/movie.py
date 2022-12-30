from flask.views import MethodView
from flask import render_template

from models import db, Movie

class MoviesList(MethodView):

    def get(self):
        movies = Movie.query.all()
        return render_template('index.html', movie_list=movies)