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
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://showApp:B00Kmy$how@127.0.0.1/bookmyshow"

db.init_app(app)
with app.app_context():
    db.create_all()

# Register `api` Blueprints
from api import routes as main_routes
app.register_blueprint(main_routes.main_bp, url_prefix='/')


# Register `view` blueprints
from views.routes import bp as views_bp
app.register_blueprint(views_bp, url_prefix='/')


if __name__ == "__main__":

  app.run(debug = True,port=8000)
