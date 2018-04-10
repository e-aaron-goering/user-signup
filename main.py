from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

username = ''
password = ''
password_confirmation = ''
email = ''

user_err = ''
password_err = ''
password_confrimation_err = ''
email_err = ''

def username_error(username):
    if not username:
        return "That's not a valid username"
    if ' ' in username:
        return "That's not a valid username"
    if 4 > len(username):
        return "That's not a valid username"
    if  len(username) > 20:
        return "That's not a valid username"
    return ''

def password_error(password):
    if not password:
        return "That's not a valid password"
    if ' ' in password:
        return "That's not a valid password"
    if 4 > len(password):
        return "That's not a valid password"
    if len(username) > 20:
        return "That's not a valid password"
    return ''

def password_confirmation_error(password, password_confirmation):
    if not password_confirmation:
        return "Passwords don't match"
    if password != password_confirmation:
        return "Passwords don't match"
    return ''

def email_error(email):
    if not email:
        return ''
    if '@' not in email:
        return "That is not a valid email address"
    if '.' not in email:
        return "That is not a valid email address"
    return ''

@app.route("/index", methods=['POST'])
def get_signup():
    username = request.form['username']
    password = request.form['password']
    password_confirmation = request.form['password-confirmation']
    email = request.form['email']

    user_err = username_error(username)
    password_err = password_error(password)
    password_confirmation_err = password_confirmation_error(password, password_confirmation)
    email_err = email_error(email)

    if user_err or password_err or password_confirmation_err or email_err:
        return render_template('index.html', user_err=user_err, password_err=password_err, 
                                password_confirmation_err=password_confirmation_err, email_err=email_err) 

    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
