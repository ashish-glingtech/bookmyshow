from unittest import result
from flask import Flask, request
from flask import render_template
import jwt
from models import db

UPLOAD_FOLDER = '/home/ankursingh/demo4/static/img'
app = Flask(__name__)


app.config["SECRET_KEY"] = "myscretkey"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://sammy:password@localhost/bookmyshow"

db.init_app(app)


# Register `api` Blueprints
from api import routes as main_routes
app.register_blueprint(main_routes.main_bp, url_prefix='/')


# Register `view` blueprints
from views.movies import movie_view_bp

app.register_blueprint(movie_view_bp, url_prefix='/')


if __name__ == "__main__":

  app.run(debug = True,port=8000)