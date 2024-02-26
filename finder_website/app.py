#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from model.subscribers import Subscriber

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'portfolio_db'
app.config['MYSQL_PASSWORD'] = 'portfolio_pwd'
app.config['MYSQL_DB'] = 'portfolio_db'

mysql = MySQL(app)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'], strict_slashes=False)
def login():
    username = request.form['username']
    password = request.form['password']

    cur = mysql.connection.cursor()
    #hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    cur.execute("SELECT * FROM subscribers WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()

    if user and bcrypt.check_password_hash(user[2], password):
        return f"Login successful for user {username}"
    else:
        return "Login failed"

@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    error_message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            error_message = "Passwords do not match. Please try again."
        else:
            cur = mysql.connection.cursor()
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cur.execute("INSERT INTO subscribers (username, password) VALUES (%s, %s)", (username, hashed_password))
            mysql.connection.commit()
            cur.close()
            
            return f"Signup successful for user {username}"

    return render_template('signup.html', error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
