from flask_restful import Resource, Api, request, reqparse
from flask import jsonify, render_template, current_app #current_app import file in the app.py inside app.conig['secret_key'] 
from models import db, User, Movie, Theater, Screen, Booking, Payment
from validation import parser, theater1, screen_val, booking_val, payment_val
from datetime import datetime, timedelta
import jwt
from functools import wraps
from flask_openid import OpenID
#module of decorated
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Token is missing'}), 403
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=['HS256'])
        except:
            return jsonify({'message' : "Token is invalid"}), 403
        return f(*args, **kwargs)
    return decorated


class Login(Resource):
    """def get_all_user(self, id):
        users = User.query.all() 
        result = []   
        for user in users:   
            user_data = {}   
            user_data['id'] = user.id  
            user_data['name'] = user.name 
            user_data['gender'] = user.gender 
            user_data['age'] = user.age 
            user_data['email'] = user.email 
            user_data['phone_no'] = user.phone_no 

            result.append(user_data)   

        return jsonify({'users': result})
"""
    @token_required
    def get(self, id):
       
        user = User.query.get(id)
        if user is None:
            return {'message': 'User not found'}, 401
        return {'message': 'Welcome {}'.format(user.name)}


def create_login(resp):
    if resp.email is None or resp.email == "":
        return {'message': 'Invalid login. Please try again.'}, 401
    user = User.query.filter_by(email=resp.email).first()
    if user is not None:
        token = jwt.encode({"some": "user name"}, current_app.config["SECRET_KEY"], algorithm="HS256",)
        return {'token': token.decode('utf-8')}, 200
    return {'message': 'User not found'}, 401

#Verify the token
class Verify(Resource):
    def post(self):
        token = jwt.encode({"some": "user name"}, current_app.config["SECRET_KEY"], algorithm="HS256",)
        print(token)
        try:
            decoded_token = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=['HS256'])
            return {'message': 'Token is valid'}, 200
        except:
            return {'message': 'Invalid token'}, 401
        
#User Module Are Here
class Users(Resource):
    def post(self):
        body_data=request.get_json()

        user=User(name=body_data['name'], gender=body_data['gender'], age=body_data['age'],
                email=body_data['email'], phone_no=body_data['phone_no'], password=body_data['password'])
        
        db.session.add(user)
        db.session.commit()
        return jsonify({"message" : "User Add succesfull"})


#Movies Module Are Here
class Movielist(Resource):
    @token_required
    def get(self, id):
        movies = Movie.query.all()
        data = []
        for movie in movies:
            data.append({'id':movie.id, 'Name': movie.name, "Detil": movie.descr, 
                        "Duration":movie.duration,"Language":movie.language, 
                        "movie_type":movie.movie_type, "image":movie.image})
        return jsonify({"Movies":data})

    def post(self):
        data = parser.parse_args()
        movie=Movie(name=data['name'], descr=data['descr'], duration=data['duration'],
                    language=data['language'], movie_type=data['movie_type'], image=data['image'])
        db.session.add(movie)
        db.session.commit()
        return jsonify({"message":"Movies Add succesfull"},)

    def put(self,id):
        data =Movie.query.filter(Movie.name=="kgf").first()
        data.image = 'movie.jpg'
       
        db.session.commit()
        return jsonify({"message":"update Movies succesfull"},)


    def delete(self,id):
        data = Movie.query.filter(Movie.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Movies succesfull"},)


#Theater Module Are Here
class Theaterlist(Resource):
    def get(self, id):
        theater = Theater.query.all()
        data = []
        for theater in theater:
            data.append({'id':theater.id, 'Name': theater.name, "location": theater.location, 
                        "rating":theater.rating,"phone_no":theater.phone_no, 
                        })
        return jsonify({"Theater":data})

    def post(self):
        data = theater1.parse_args()
        theater=Theater(name=data['name'], location=data['location'], rating=data['rating'],
                        phone_no=data['phone_no'])
        db.session.add(theater)
        db.session.commit()
        return jsonify({"message" : "Theater Add succesfull"})

    def put(self,id):
        data =Theater.query.filter(Theater.name=="GIP").first()
        data.rating = '5 star'
       
        db.session.commit()
        return jsonify({"message":"update Theater succesfull"},)


    def delete(self,id):
        data = Theater.query.filter(Theater.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Theater succesfull"},)


#Screen Module Are Here
class Screenlist(Resource):

    def get(self, id):
        screen = Screen.query.all()
        data = []
        for screen in screen:
            data.append({"id":screen.id, "movie_id": screen.movie_id, "theater_id": screen.theater_id,
                        "nane":screen.name, "ticket_type":screen.ticket_type,
                        "total_seats":screen.total_seats, 
                        })
        return jsonify({"Screen":data})

    def post(self):
        
        data = screen_val.parse_args()
       
        screen=Screen(name=data['name'], movie_id=data['movie_id'], theater_id=data['theater_id'],
                      ticket_type=data['ticket_type'], total_seats=data['total_seats'])
        db.session.add(screen)
        db.session.commit()
        return jsonify({"message" : "Screen Add succesfull"})

    def put(self,id):
        data =Screen.query.filter(Screen.id=="4").first()
        data.name = 'Audi2'
        db.session.commit()
        return jsonify({"message":"update Screen succesfull"},)


    def delete(self,id):
        data = Screen.query.filter(Screen.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Screen succesfull"},)

#Booking Module Are Here
class Bookinglist(Resource):

    def get(self, id):
        booking = Booking.query.all()
        data = []
        for booking in booking:
            data.append({"id":booking.id, "screen_id": booking.screen_id, "user_id": booking.user_id,
                        "booking_no":booking.booking_no, "date":booking.date,
                        "start_time":booking.start_time, "end_time":booking.end_time,
                        "payment":booking.payment, "status":booking.status
                        })
        return jsonify({"Booking":data})

    def post(self):

        data = booking_val.parse_args()

        booking=Booking(screen_id=data['screen_id'], user_id=data['user_id'], 
                        booking_no=data['booking_no'], date=data['date'], start_time=data['start_time'],
                        end_time=data['end_time'], payment=data['payment'], status=data['status'])
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message" : "Booking Add succesfull"})

    def put(self,id):
        data =Booking.query.filter(Booking.booking_no =="BO002").first()
        data.status  = 'Done'
        db.session.commit()
        return jsonify({"message":"update Booking succesfull"})


    def delete(self,id):
        data = Booking.query.filter(Booking.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Booking succesfull"})

#Payment Module Are Here
class Paymentlist(Resource):
    def get(self, id):
        payment = Payment.query.all()
        data = []
        for payment in payment:
            data.append({"id":payment.id, "payment_type": payment.payment_type, "booking_id": payment.booking_id,
                        "user_id":payment.user_id, "amount":payment.amount, "date":payment.date,
                        })
        return jsonify({"Payment":data})

    def post(self):
        #data = request.get_json()
        data = payment_val.parse_args()
        
        payment = Payment(payment_type=data['payment_type'], booking_id=data['booking_id'],
                          user_id=data['user_id'], amount=data['amount'], date=data['date'])
        db.session.add(payment)
        db.session.commit()
        return jsonify({"message" : "Payment Add succesfull"})

    
    def put(self,id):
        data =Payment.query.filter(Payment.booking_id =="3").first()
        data.amount  = '499'
        db.session.commit()
        return jsonify({"message":"update Payment succesfull"})


    def delete(self,id):
        data = Booking.query.filter(Payment.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Payment succesfull"})
