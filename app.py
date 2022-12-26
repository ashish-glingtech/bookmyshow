from unittest import result
from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)

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

class User_list(Resource):
    def post(self):
        body_data=request.get_json()
        user=User(name = body_data['name'], gender = body_data['gender'], age = body_data['age'], email = body_data['email'], phone_no = body_data['phone_no'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message" : "User Add succesfull"})

class Movie_list(Resource):
    def post(self):
        data = request.get_json()
        movie=Movie(name = data['name'], descr = data['descr'], duration = data['duration'], language = data['language'], movie_type = data['movie_type'])
        db.session.add(movie)
        db.session.commit()
        return jsonify({"message" : "Movies Add succesfull"})

class Theater_list(Resource):
    def post(self):
        data = request.get_json()
        theater=Theater(name = data['name'], location = data['location'], rating = data['rating'], phone_no = data['phone_no'])
        db.session.add(theater)
        db.session.commit()
        return jsonify({"message" : "Theater Add succesfull"})

class Screen_list(Resource):
    def post(self):
        data = request.get_json()
        screen=Screen(name = data['name'], movie_id = data['movie_id'], theater_id = data['theater_id'], ticket_type = data['ticket_type'], total_seats = data['total_seats'])
        db.session.add(screen)
        db.session.commit()
        return jsonify({"message" : "Screen Add succesfull"})


class Booking_list(Resource):
    def post(self):
        data = request.get_json()
        booking=Booking(screen_id = data['screen_id'], user_id = data['user_id'], booking_no = data['booking_no'], date = data['date'], start_time = data['start_time'], end_time = data['end_time'], payment = data['payment'], status = data['status'])
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message" : "Booking Add succesfull"})


class PaymentList(Resource):

    def post(self):
        data = request.get_json()
        payment = Payment(payment_type=data['payment_type'], booking_id = data['booking_id'],
                        user_id = data['user_id'], amount = data['amount'], date = data['date'])
        db.session.add(payment)
        db.session.commit()
        return jsonify({"message" : "Payment Add succesfull"})


api.add_resource(User_list, '/login')
api.add_resource(Movie_list, '/movies')
api.add_resource(Theater_list, '/theater')
api.add_resource(Screen_list, '/screen')
api.add_resource(Booking_list, '/booking')
api.add_resource(PaymentList, '/payment')


if __name__ == "__main__":

  app.run(debug = True,port=8000)