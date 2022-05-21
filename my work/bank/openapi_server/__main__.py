#!/usr/bin/env python3


import bcrypt
import connexion
import re
import mysql.connector
import MySQLdb.cursors
import os
from openapi_server import encoder
from mysql.connector import errorcode
from flask import Flask, render_template, request, redirect, url_for, session#, jsonify
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



try:
  cnx = mysql.connector.connect(user='root',
                                password='cs-ner',
                                host='localhost',
                                database='base'
                                )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()





# flask_app = Flask(__name__)
app = connexion.App(__name__, specification_dir='./openapi/')

app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': ' Bank'},
            pythonic_params=True)

flask_app=app.app

bcrypt = Bcrypt(flask_app)
flask_app.config["SESSION_PERMANENT"] = False
flask_app.config["SESSION_TYPE"] = "filesystem"

flask_app.secret_key = 'secret'

mysql = MySQL(flask_app)

flask_app.config['MYSQL_HOST'] = 'localhost'
flask_app.config['MYSQL_USER'] = 'root'
flask_app.config['MYSQL_PASSWORD'] = 'cs-ner'
flask_app.config['MYSQL_DB'] = 'base'    


basedir = os.path.abspath(os.path.dirname(__file__))
# Database
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cs-ner2121@localhost/'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(flask_app)
# Init ma
ma = Marshmallow(flask_app)

class Balance(db.Model):
  account_id = db.Column(db.Integer, primary_key=True)
  money = db.Column(db.Float)

  def __init__(self, money):
    self.money = money

class balanceSchema(ma.Schema):
  class Meta:
    fields = ('id', 'money')

# Init schema
balance_schema = balanceSchema()
balances_schema = balanceSchema(many=True)




@flask_app.route('/balance', methods=['POST'])
def add_balance():
  money = request.json['money']

  new_balance = Balance(money,)

  db.session.add(new_balance)
  db.session.commit()

  return balance_schema.jsonify(new_balance)


@flask_app.route('/')
def index():
    bal=''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT money FROM balance JOIN accounts ON accounts.id = account_id WHERE username = % s', (session['username'],))
    score = cursor.fetchone()
    bal=str(score).replace("{'money':",'').replace("}",'')
    if not session.get("username"):
        return redirect("/login")
    return render_template('index.html',bal=bal)



# @flask_app.route('/balance', methods=['GET', 'POST'])
# def balance():
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('SELECT money FROM balance JOIN accounts ON accounts.id = account_id WHERE username = % s', (session['username'],))
#     score = cursor.fetchone() 
# #     return render_template('index.html', bal=str(score).replace("{'money':",'').replace("}",''))


@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        hashed = bcrypt.generate_password_hash(password.encode('utf8'))
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s ', [username])
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            bcrypt.check_password_hash(hashed, account['password'])
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@flask_app.route('/logout')
def logout():
    session["username"] = None
    return redirect("/")

@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'first_name' in request.form and 'last_name' in request.form and 'phone' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        phone = request.form['phone']
        hashed = bcrypt.generate_password_hash('password')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username,))
        accounte = cursor.fetchone()
        if accounte:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts (id, username, passw, email, first_name, last_name, phone) VALUES (NULL, % s, % s, % s, % s, % s, % s)', (username, hashed, email, first_name, last_name, phone ))
            cursor.execute('INSERT INTO balance (account_id, money) VALUES (LAST_INSERT_ID(), 0)')
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@flask_app.route('/trans', methods=['POST'])
def trans():
    username_po = request.form["username_po"]
    money = request.form['money']
    cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor1.execute('UPDATE balance JOIN accounts ON accounts.id = account_id SET money = money - % s WHERE username = % s;', (money ,session['username']))
    cursor1.execute('UPDATE balance JOIN accounts ON accounts.id = account_id SET money = money + % s WHERE username = % s;', (money ,username_po))
    mysql.connection.commit()
    return render_template('trans.html')

if __name__ == '__main__':

    flask_app.run(port=8080)
