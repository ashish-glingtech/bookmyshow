from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
from datetime import datetime

datetime.utcnow()

db=SQLAlchemy()


class User(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(200),nullable=False)
    gender=db.Column(db.String(50),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    email= db.Column(db.String(200),nullable=False)
    phone_no = db.Column(db.String(300),nullable=False)
   
    

    def __repr__(self) -> str:
        return f"{self.name}"

class Movie(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(50),nullable=False)
    descr=db.Column(db.String(90),nullable=False)
    duration=db.Column(db.String(100),nullable=False)
    language= db.Column(db.String(50),nullable=False)
    movie_type = db.Column(db.String(50),nullable=False)
   
    def __repr__(self) -> str:
        return f"{self.name}"

class Theater(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(50),nullable=False)
    location=db.Column(db.String(100),nullable=False)
    rating= db.Column(db.String(50),nullable=False)
    phone_no = db.Column(db.Integer,nullable=False)
   
    def __repr__(self) -> str:
        return f"{self.name}"


class Booking(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    screen_id= db.Column(db.Integer, db.ForeignKey('parent.id'))
    user_id=db.Column(db.Integer,nullable=False)
    booking_no= db.Column(db.String(50),nullable=False)
    date = db.Column(db.Integer,nullable=False)
    start_time = db.Column(db.String(50),nullable=False)
    end_time  = db.Column(db.String(50),nullable=False)
    payment = db.Column(db.String(50),nullable=False)
    status  = db.Column(db.String(50),nullable=False)
    
   
    def __repr__(self) -> str:
        return f"{self.name}"