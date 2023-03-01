import os

from flask import (Flask, )
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
mail = Mail(app)
    
app.config['SECRET_KEY'] = 'very-secret-key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@localhost/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.mail.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_USE_TLS '] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


mail.init_app(app)
db.init_app(app)
with app.app_context():
    db.create_all()


MAIL_SERVER = 'smtp.mail.ru'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv("EMAIL")
MAIL_PASSWORD = os.getenv("PASSWORD")

