from flask import render_template, Blueprint

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  return render_template('users/register.html', title='register')

@users.route('/login', methods=['GET','POST'])
def login():
  return render_template('users/login.html', title='login')


