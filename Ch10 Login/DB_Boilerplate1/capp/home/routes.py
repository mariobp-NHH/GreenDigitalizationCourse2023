from flask import render_template, Blueprint
from capp.models import User, Transport

home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_home():
  user1 = User.query.first().username
  transport1 = Transport.query.first().kms
  user3 = User.query.filter_by(username='Bjørk').first().username
  user4 = User.query.filter_by(username='Bjørk').first()
  transports = Transport.query.filter_by(user_id=user4.id)
  users = User.query.all()
  return render_template('home.html', user1=user1, transport1=transport1, user3=user3, transports=transports, users=users)