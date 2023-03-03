from flask_restful import Resource, Api, request, reqparse
from flask import jsonify, render_template, current_app #current_app import file in the app.py inside app.conig['secret_key'] 
from models import db, User, Movie, Theater, Screen, Booking, Payment, Actor, Crew, Otp
from validation import parser, theater1, screen_val, booking_val, payment_val, actor_val, crew_val, otp_val, user_val
from datetime import datetime, timedelta
import jwt
from functools import wraps
from flask_openid import OpenID
from werkzeug.utils import secure_filename
import os
from twilio.rest import Client
import jwt
import random
import string
import time


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Your Twilio account SID and Auth Token
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Create a Twilio client
client = Client(account_sid, auth_token)


class OtpSave(Resource):

    def post(self):
        data = otp_val.parse_args()
        otp_gen = ''.join(random.choices(string.digits, k=6))
        timestamp = time.time()
        tp=Otp(phone_number=data['phone_number'], otp=otp_gen, timestamp=timestamp)
        # Send an SMS message with the OTP
        message = client.messages.create(
            to="+91" + str(data['phone_number']), # Your recipient's phone number
            from_="+14782495642", # Your Twilio phone number
            body=f"Your OTP is: {otp_gen}"
        )
        db.session.add(tp)
        db.session.commit()
        return "Verification code sent!", 200

    def put(self):
        data = otp_val.parse_args()
        phone_number = data.get('phone_number')
        if phone_number is None:
            return 'phone_number is required.', 400

        otp = Otp.query.filter_by(phone_number=phone_number).first()
        if otp is None:
            return 'No OTP found for the specified user.', 404

        otp_gen = ''.join(random.choices(string.digits, k=6))
        timestamp = time.time()
        tp=Otp(phone_number=data['phone_number'], otp=otp_gen, timestamp=timestamp)
        # Send an SMS message with the OTP
        message = client.messages.create(
            to="+91" + str(data['phone_number']), # Your recipient's phone number
            from_="+14782495642", # Your Twilio phone number
            body=f"Your OTP is: {otp_gen}"
        )
        db.session.add(tp)
        db.session.commit()
        return "Verification code sent!", 200


class OtpReset(Resource):

    def get(self):
        data = otp_val.parse_args()
        phone_number = data.get('phone_number')
        print(phone_number)
        result=Otp.query.filter_by(phone_number=phone_number).delete()
        if phone_number is None:
            return 'phone_number  is required.', 400
       
        db.session.add(result)
        db.session.commit()
        return Otplist()
    

class OtpVerify(Resource):

    def post(self):
        data = request.get_json()
        phone_number = data.get('phone_number')
        otp = data.get('otp')
        user = Otp.query.filter_by(phone_number=phone_number).order_by(Otp.timestamp.desc()).first()
        if not user:
            return {'message': 'User phone number not found.'}, 404
        if user.otp != otp:
            return {'message': 'Incorrect Otp.'}, 401
        if time.time() - user.timestamp > 120: # OTP is valid for 120 seconds
            return {'message': 'Otp expired'}, 401
        token = jwt.encode({'user_id': user.otp_id, 'phone_number': user.phone_number}, current_app.config["SECRET_KEY"])

        return {'message': 'Login successful.'}, 200
        

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
    #@token_required
    def get(self, id):
        user = User.query.get(id)
        if user is None:
            return {'message': 'User not found'}, 401
        return {'message': 'Welcome {}'.format(user.name)}

        
#User Module Are Here
class Users(Resource):
    def post(self):
        #body_data=request.get_json()
        data = user_val.parse_args()
        users=User(name=data['name'], gender=data['gender'], age=data['age'],
                email=data['email'], phone_no=data['phone_no'], password=data['password'])
        
        db.session.add(users)
        db.session.commit()
        return jsonify({"message" : "User Add succesfull"})


#Movies Module Are Here
class Image(Resource):

    def post(self):
	# check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'error' : 'No file part in the request'}), 400
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message' : 'File successfully uploaded'})
            

class MovieStore(Resource):

    def get(self):
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


class MovieList(Resource):
    #@token_required
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
class TheaterStore(Resource):

    def get(self):
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


class TheaterList(Resource):
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
class ScreenStore(Resource):

    def get(self):
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

class ScreenList(Resource):
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
class BookingStore(Resource):

    def get(self):
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


class BookingList(Resource):

    def put(self,id):
        data =Booking.query.filter(Booking.booking_no =="B0003").first()
        data.status  = 'Done'
        db.session.commit()
        return jsonify({"message":"update Booking succesfull"})

    def delete(self,id):
        data = Booking.query.filter(Booking.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Booking succesfull"})


#Payment Module Are Here
class PaymentStore(Resource):
    def get(self):
        payment = Payment.query.all()
        data = []
        for payment in payment:
            data.append({"id":payment.id, "payment_type": payment.payment_type, "booking_id": payment.booking_id,
                        "user_id":payment.user_id, "amount":payment.amount, "date":payment.date,
                        })
        return jsonify({"Payment":data})

    def post(self):
        data = payment_val.parse_args()
        payment = Payment(payment_type=data['payment_type'], booking_id=data['booking_id'],
                          user_id=data['user_id'], amount=data['amount'], date=data['date'])
        db.session.add(payment)
        db.session.commit()
        return jsonify({"message" : "Payment Add succesfull"})


class PaymentList(Resource):
    def put(self,id):
        data =Payment.query.filter(Payment.booking_id =="8").first()
        data.amount  = '500'
        db.session.commit()
        return jsonify({"message":"update Payment succesfull"})

    def delete(self,id):
        data = Booking.query.filter(Payment.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Payment succesfull"})

#Actor Module Are Here
class ActorStore(Resource):

    def get(self):
        actor = Actor.query.all()
        data = []
        for actor in actor:
            data.append({"id":actor.id, "name": actor.name, "image": actor.image,
                        "actor_type":actor.actor_type, "movie_id":actor.movie_id,
                        })
        return jsonify({"Payment":data})

    def post(self):        
        data = actor_val.parse_args()
        if data.image:
            image=data.image
        image.save(os.path.join(current_app.config["UPLOAD_FOLDER"], secure_filename(image.filename)))
        actor = Actor(name=data['name'], image=data['image'],
                actor_type=data['actor_type'], movie_id=data['movie_id'])
                          
        db.session.add(actor)
        db.session.commit()
        return jsonify({"message" : "Actor Add succesfull"})


class ActorList(Resource):
    def post(self):        
        data = actor_val.parse_args()
        if data.image:
            image=data.image
        image.save(os.path.join(current_app.config["UPLOAD_FOLDER"], secure_filename(image.filename)))
        actor = Actor(name=data['name'], image=data['image'],
                          actor_type=data['actor_type'], movie_id=data['movie_id'])
                          
        db.session.add(actor)
        db.session.commit()
        return jsonify({"message" : "Actor Add succesfull"})

    def put(self,id):
        data =Actor.query.filter(Actor.id =="2").first()
        data.name  = 'shahrukh'
        db.session.commit()
        return jsonify({"message":"update Actor succesfull"})

    def delete(self,id):
        data = Actor.query.filter(Actor.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Actor succesfull"})


#Crew Module Are Here
class CrewStore(Resource):

    def get(self):
        crew = Crew.query.all()
        data = [] 
        for crew in crew:
            data.append({"id":crew.id, "name": crew.name, "image": crew.image,
                        "crew_type":crew.crew_type, "movie_id":crew.movie_id,
                        })
        return jsonify({"Payment":data})

    def post(self):
        data = crew_val.parse_args()
        if data.image:
            image=data.image
            print(image)
        image.save(os.path.join(current_app.config["UPLOAD_FOLDER"], secure_filename(image.filename)))
        crew = Crew(name=data['name'], image=data['image'],
                          crew_type=data['crew_type'], movie_id=data['movie_id'])
        db.session.add(crew)
        db.session.commit()
        return jsonify({"message" : "Crew Add succesfull"})


class CrewList(Resource):

    def put(self,id):
        data =Crew.query.filter(Crew.id =="1").first()
        data.name  = 'Bosco Caeser'
        db.session.commit()
        return jsonify({"message":"update Crew succesfull"})

    def delete(self,id):
        data = Crew.query.filter(Crew.id==id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({"message":"Delete Crew succesfull"})
