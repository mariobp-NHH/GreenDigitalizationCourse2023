from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html')

@application.route('/methodology')
def methodology():
  return render_template('methodology.html', title='methodology')

@application.route('/carbon_app')
def carbon_app():
    return render_template('carbon_app.html', title='carbon_app')

if __name__=='__main__':
  application.run(debug=True)  