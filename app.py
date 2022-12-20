from unittest import result
from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
  


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://sammy:password@localhost/bookmyshow"





result=[

  {

    'id':1,
    'name':'ankur',
    'gender':'male',
    'email':'ankur@gmail.com',
    'phone_no':'33533333'

  }

]


@app.route('/login')
def login():
  
  return jsonify({'login':result})

@app.route('/login/<string:name>')
def get_login(name):
  for data in result:
    if data['name'] == name:
      return jsonify(data)
    
  return jsonify({'message':'data not found'})

from models import db, User, Movie, Theater, Screen, Booking, Payment

db.init_app(app)

@app.route('/login', methods = ['POST'])
def create_login():
  body_data=request.get_json()
  #result.append(body_data)
  user=User(name = body_data['name'], gender = body_data['gender'], age = body_data['age'], email = body_data['email'], phone_no = body_data['phone_no'])
  db.session.add(user)
  db.session.commit()
 
  print(body_data['name'])

  return jsonify({"message" : "User create succesfull"})

@app.route('/movies', methods = ['POST'])
def add_movie():
  data = request.get_json()
  movie=Movie(name = data['name'], descr = data['descr'], duration = data['duration'], language = data['language'], movie_type = data['movie_type'])

  db.session.add(movie)
  db.session.commit()
 
  return jsonify({"message" : "Movies Add succesfull"})



@app.route('/theater', methods = ['POST'])
def add_theater():
  data = request.get_json()
  theater=Theater(name = data['name'], location = data['location'], rating = data['rating'], phone_no = data['phone_no'])
  
  db.session.add(theater)
  db.session.commit()
 
  return jsonify({"message" : "Theater Add succesfull"})


@app.route('/screen', methods = ['POST'])
def add_screen():
  data = request.get_json()
  screen=Screen(name = data['name'], movie_id = data['movie_id'], theater_id = data['theater_id'], ticket_type = data['ticket_type'], total_seats = data['total_seats'])

  db.session.add(screen)
  db.session.commit()
 
  return jsonify({"message" : "Screen Add succesfull"})


@app.route('/booking', methods = ['POST'])
def add_booking():
  data = request.get_json()
  booking=Booking(screen_id = data['screen_id'], user_id = data['user_id'], booking_no = data['booking_no'], date = data['date'], start_time = data['start_time'], end_time = data['end_time'], payment = data['payment'], status = data['status'])
  db.session.add(booking)
  db.session.commit()
 
  return jsonify({"message" : "Booking Add succesfull"})


@app.route('/payment', methods = ['POST'])
def add_payment():
  data = request.get_json()
  payment=Payment(payment_type = data['payment_type'], booking_id = data['booking_id'], user_id = data['user_id'], amount = data['amount'], date = data['date'])

  db.session.add(payment)
  db.session.commit()
 
  return jsonify({"message" : "Payment Add succesfull"})


if __name__ == "__main__":

  app.run(debug = True,port=8000)