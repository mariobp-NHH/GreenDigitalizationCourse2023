from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html')

@application.route('/methodology')
def methodology():
  return render_template('methodology.html', title='methodology')

@application.route('/app_calculator')
def app_calculator():
    return render_template('app_calculator.html', title='app_calculator')

if __name__=='__main__':
  application.run(debug=True)  