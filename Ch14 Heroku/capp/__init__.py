from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

### Code GitHub
application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
# DBVAR=os.environ['DATABASE_URL']
# DBVAR="postgresql://osgiedhtruutkx:os.environ.get(‘DB_PASSWORD’)@ec2-52-215-68-14.eu-west-1.compute.amazonaws.com:5432/d8scuqpg5glq3f"
DBVAR="postgresql://osgiedhtruutkx:835d46742b5eaba7a35135c701e4137b122ea454437d97d958238ffbe416457a@ec2-52-215-68-14.eu-west-1.compute.amazonaws.com:5432/d8scuqpg5glq3f"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

### Code computer
application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'
DBVAR="postgresql://osgiedhtruutkx:835d46742b5eaba7a35135c701e4137b122ea454437d97d958238ffbe416457a@ec2-52-215-68-14.eu-west-1.compute.amazonaws.com:5432/d8scuqpg5glq3f"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

