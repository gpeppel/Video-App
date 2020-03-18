import MySQLdb
# from dbconnect import connection
from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc

def connection():
    conn = MySQLdb.connect(host="myserver",
                           user="greg",
                           passwd="greg",
                           db="videoapp")
    c = conn.cursor()

    return c, conn

def connect_login():
    try:
        c, conn = connection()
        return "okay"
    except Exception as e:
        return str(e)


def login_page():
    try:
        if request.method == "POST":
            details = request.form
            email = details['email']
            password = details['password']

            c, conn = connection()

            x = c.execute("SELECT * FROM `user_login` WHERE email = (%s) AND password = (%s);", (thwart(email), thwart(password)))

            if int(x) > 0:
                
                s = c.execute("SELECT full_name FROM user_login WHERE email = (%s) AND password = (%s);", (thwart(email), thwart(password)))

                conn.commit()
                flash("Success!  Hi, " + str(s))
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['email'] = email

                return redirect(url_for('index.html'))

            else:
                flash("Sorry, but I couldn't find anything")
                return render_template('login.html')

        return render_template('login.html')

    except Exception as e:
        return str(e)
