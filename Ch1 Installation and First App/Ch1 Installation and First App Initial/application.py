from flask import Flask
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
    return "<h1>Welcome home!</h1>" \
    "<p>This is our methodology:</p> <button>Link</button>" \
    "<ul>" \
    " <li>Developer 1...</li>" \
    " <li>Developer 2...</li>" \
    " <li>Developer 3...</li>" \
    "</ul>"


@application.route('/methodology')
def methodology():
    return "<h1>Methodology</h1>"

@application.route('/carbon_app')
def carbon_app():
    return "<h1>Carbon App</h1>"

if __name__ =='__main__':
    application.run(debug=True)
