from flask import Flask, Blueprint, request, jsonify, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json

api = Blueprint("api", __name__)

# Declaring the model.
db = SQLAlchemy()
ma = Marshmallow()


class Users(db.Model):
    __tablename__ = "userAuth"
    UserID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Email = db.Column(db.Text)
    Password = db.Column(db.Text)

    def __init__(self, Email, Password, UserID = None):
        self.UserID = UserID
        self.Email = Email
        self.Password = Password


class UserSchema(ma.Schema):
    
    class Meta:
        fields = ("UserID", "Email", "Password")

singleUserSchema = UserSchema()
userSchema = UserSchema(many = True)

class WeatherMonitoringSystem:

    @api.route("/api/login", methods = ["POST"])
    def verifyCredentials():
        query = Users.query.all()
        result = userSchema.dump(query)
        # return jsonify(result.data) for development
        return jsonify(result)
   

    @api.route("/api/register", methods = ["POST"])
    def newCredentials():
        Email = request.json["Email"]
        Password = request.json["Password"]
        newUser = Users(Email = Email, Password = Password)

        db.session.add(newUser)
        db.session.commit()
        return True
