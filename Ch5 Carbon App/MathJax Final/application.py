from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html')

if __name__=='__main__':
  application.run(debug=True)  