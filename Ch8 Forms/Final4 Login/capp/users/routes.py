from flask import render_template, Blueprint, redirect, flash, url_for
from capp.users.forms import RegistrationForm, LoginForm

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      flash('Your account has been created! Now, you are able to login!', 'success')
      return redirect(url_for('home.home_home'))
  return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'fjell@demo.com' and form.password.data == 'regn':
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect(url_for('home.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('users/login.html', title='login', form=form)


