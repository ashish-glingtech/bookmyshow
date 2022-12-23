from unittest import result
from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from api import routes as main_routes
from models import db


app = Flask(__name__)


app.config['SECRET_KEY'] = 'any secret string'
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://sammy:password@localhost/bookmyshow"

db.init_app(app)

# Register Blueprints
app.register_blueprint(main_routes.main_bp, url_prefix='/')


if __name__ == "__main__":

  app.run(debug = True,port=8000)