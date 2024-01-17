from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html', title='Home')

@application.route('/methodology')
def methodology():
    return render_template('methodology.html', title='Methodology two')

@application.route('/carbon_app')
def carbon_app():
    return "<p>Carbon App web page</p>"

if __name__=='__main__':
  application.run(debug=True)  