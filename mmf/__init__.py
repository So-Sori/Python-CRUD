from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
img = '/Users/Soribel/Desktop/Python Crud/mmf/img'
app.config["UPLOAD_FOLDER"] = img
app.config['SECRET_KEY'] = 'b62f0b4639854a0f07b98b59de917650757215fd6ba4b1d4cf234ed3e0a4ef7a8d3c5c8171da0ae9'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../mmf/database_page.db'
db = SQLAlchemy(app)
app.app_context().push()


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from mmf import routes