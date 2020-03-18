from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from static import login

app = Flask(__name__)

login.connect_login()

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def sign_in():
	return login.login_page()

if __name__ == "__main__":
    app.run("192.168.156.131", debug = True)