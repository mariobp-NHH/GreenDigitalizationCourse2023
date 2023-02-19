from flask import Flask

application = Flask(__name__) 

    
@application.route('/')
@application.route('/home')
def home():
  return "<h1>Welcome Home</h1>"

if __name__=='__main__':
  application.run(debug=True) 