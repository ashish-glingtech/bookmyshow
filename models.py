from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
from datetime import datetime

datetime.utcnow()

db=SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone_no = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    booking = db.relationship('Booking', backref='User', lazy='dynamic')
    payment = db.relationship('Payment', backref='User', lazy='dynamic')
   
    def __repr__(self) -> str:
        return f"{self.name}"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    descr = db.Column(db.String(90), nullable=False)
    duration = db.Column(db.String(100),nullable=False)
    language = db.Column(db.String(50),nullable=False)
    movie_type = db.Column(db.String(50),nullable=False)
    image = db.Column(db.String(100),nullable=False)
    screen = db.relationship('Screen', backref='movie', lazy='dynamic')
    actor = db.relationship('Actor', backref='movie', lazy='dynamic')
    crew = db.relationship('Crew', backref='movie', lazy='dynamic')
    
    def __repr__(self) -> str:
        return f"<Movie {self.id}>"


class Theater(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.Integer, nullable=False)
    screen = db.relationship('Screen', backref='theater', lazy='dynamic')
   
    def __repr__(self) -> str:
        return f"{self.name}"


class Screen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ticket_type = db.Column(db.String(100), nullable=False)
    total_seats = db.Column(db.String(50), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'))
    booking = db.relationship('Booking', backref='Screen', lazy='dynamic')
   
    def __repr__(self) -> str:
        return f"{self.name}"


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    booking_no = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time  = db.Column(db.String(50), nullable=False)
    payment = db.Column(db.String(50), nullable=False)
    status  = db.Column(db.String(50), nullable=False)
    payments = db.relationship('Payment', backref='Booking', lazy='dynamic')
    
    def __repr__(self) -> str:
        return f"{self.id}"


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_type = db.Column(db.String(50), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}"

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    image = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(50), nullable=False)
    actor_type = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}"

class Crew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    image = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(50), nullable=False)
    crew_type = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}"

class Otp(db.Model):
    otp_id  = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(120), nullable=False)
    otp = db.Column(db.Integer,nullable=False)
    timestamp = db.Column(db.Float, nullable=False)

    
    
