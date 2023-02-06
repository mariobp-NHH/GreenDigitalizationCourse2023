from flask import render_template, Blueprint

users=Blueprint('users',__name__)

@users.route('/register')
def register():
  return render_template('users/register.html', title='register')

@users.route('/login')
def login():
  name='Mario'
  return render_template('users/login.html', title='login', name=name)