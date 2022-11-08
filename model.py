from flask import Flask, render_template, request , url_for,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key="hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Crownn_Plaza.db'
db = SQLAlchemy(app)

class Room_booking(db.Model):
    Room_NO = db.Column(db.Integer, primary_key=True)
    Room_type = db.Column(db.String(5), nullable=False)
    Check_in_Date = db.Column(db.String(15), nullable=True)
    Check_out_Date = db.Column(db.String(15), nullable=False)
    No_of_days = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Mobile_no = db.Column(db.String(15), nullable=False)
    Id_Proof = db.Column(db.String(15), nullable=False)
    Id_No = db.Column(db.String(15), nullable=False)
    Male = db.Column(db.Integer, nullable=False)
    Female = db.Column(db.Integer, nullable=False)
    Child = db.Column(db.Integer, nullable=False)


class Admin(db.Model):
    RoomNo = db.Column(db.Integer, primary_key=True)
    RoomType = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(15), nullable=False)

class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True, )
    UserName = db.Column(db.String(60), nullable=False)
    Email = db.Column(db.String(60), nullable=False)
    Password = db.Column(db.String(60), nullable=False)
