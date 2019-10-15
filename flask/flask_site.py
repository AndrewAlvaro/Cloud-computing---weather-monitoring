from flask import Flask, Blueprint, request, jsonify, render_template, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
import random

site = Blueprint("site", __name__)


@site.route('/')
def landing():
    if not session.get('logged_in'):
        return render_template('landing.html')
    else:
        return render_template('home.html')
    

@site.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('landing.html')
    else:
        return render_template('home.html')

@site.route('/report')
def report():
    if not session.get('logged_in'):
        return render_template('landing.html')
    else:
        return render_template('report.html')

@site.route('/login', methods=["GET"])
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@site.route('/login', methods=["POST"])
def loginPOST():
    Email = request.form.get("email")
    Password = request.form.get("password")
    
    response = requests.post("http://directed-strata-237809.appspot.com/api/login")
    data = json.loads(response.text)
    
    for credentials in data:
        if credentials['Email'] == Email and credentials['Password'] == Password:
            session['logged_in'] = True
            return render_template('home.html')
            break
  
    flash('Credentials invalid! Please try again')
    return redirect('/login')

@site.route('/register', methods=["GET"])
def register():
    if not session.get('logged_in'):
        return render_template('register.html')
    else:
        return render_template('home.html')

@site.route('/register', methods=["POST"])
def registerPOST():

    Email = request.form.get("email")
    Password = request.form.get("password")
    ConfirmPassword = request.form.get("confirmpassword")
    
    if(Password != ConfirmPassword):
        flash('Password did not match!')
        return redirect('/register')
    else:

        data = {
            "Email": Email,
            "Password": Password
        }

        headers = {
            "Content-type": "application/json"
        }

        response = requests.post("http://directed-strata-237809.appspot.com/api/register", data = json.dumps(data), headers = headers)
        flash('You are registered!')
        return redirect('/register')

@site.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/')