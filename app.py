import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from models import db 

load_dotenv()
UPLOAD_FOLDER = '/home/ankursingh/demo4/static/img'
app = Flask(__name__)


app.config["SECRET_KEY"] = "myscretkey"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI']= os.environ['MYSQL_CONNECTION_URL']


db.init_app(app)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

# Register `api` Blueprints
from api import routes as main_routes
app.register_blueprint(main_routes.main_bp, url_prefix='/api')


# Register `view` blueprints
from views.routes import bp as views_bp
app.register_blueprint(views_bp, url_prefix='/')


if __name__ == "__main__":

  app.run(debug = True,port=8000)
