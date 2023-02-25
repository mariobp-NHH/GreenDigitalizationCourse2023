from flask import render_template, Blueprint
from capp.models import Transport
from flask_login import login_required

carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

@carbon_app.route('/carbon_app/new_entry')
@login_required
def new_entry():
    return render_template('carbon_app/new_entry.html', title='new_entry')

@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    return render_template('carbon_app/your_data.html', title='your_data')
    