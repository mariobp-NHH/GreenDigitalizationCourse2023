from flask import render_template, Blueprint

carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route('/carbon_app')
def carbon_app_home():
    return render_template('carbon_app.html', title='carbon_app')
    