from flask import render_template, Blueprint
from capp.models import User, Transport

home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_home():
  return render_template('home.html')