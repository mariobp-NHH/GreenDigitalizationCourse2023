from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__) 

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carbon_app.db'
db = SQLAlchemy(application)

class User(db.Model):
  __tablename__ = "user_table"
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(30), unique=True, nullable=False)
  transport = db.relationship('Transport', backref='author', lazy=True)

class Transport(db.Model):
  __tablename__= 'transport_table'
  id = db.Column(db.Integer, primary_key=True)
  kms = db.Column(db.Float)
  user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    
@application.route('/')
@application.route('/home')
def home():
  return "<h1>Welcome Home</h1>"

if __name__=='__main__':
  application.run(debug=True) 