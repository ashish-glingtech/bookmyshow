from flask_restful import Resource, Api, request, reqparse
from flask import jsonify, render_template
from models import db, User, Movie, Theater, Screen, Booking, Payment
from validation import parser, theater1, screen_val, booking_val, payment_val



class Users(Resource):
    def post(self):
        body_data=request.get_json()

        user=User(name=body_data['name'], gender=body_data['gender'], age=body_data['age'],
                email=body_data['email'], phone_no=body_data['phone_no'])

        db.session.add(user)
        db.session.commit()
        return jsonify({"message" : "User Add succesfull"})

#Movies Module Are Here
class Movielist(Resource):

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
    def post(self):
        data = theater1.parse_args()
        theater=Theater(name=data['name'], location=data['location'], rating=data['rating'],
                        phone_no=data['phone_no'])
        db.session.add(theater)
        db.session.commit()
        return jsonify({"message" : "Theater Add succesfull"})


#Screen Module Are Here
class Screenlist(Resource):
    def post(self):
        
        data = screen_val.parse_args()
       
        screen=Screen(name=data['name'], movie_id=data['movie_id'], theater_id=data['theater_id'],
                      ticket_type=data['ticket_type'], total_seats=data['total_seats'])
        db.session.add(screen)
        db.session.commit()
        return jsonify({"message" : "Screen Add succesfull"})


#Booking Module Are Here
class Bookinglist(Resource):
    def post(self):
        
        data = booking_val.parse_args()
        
        booking=Booking(screen_id=data['screen_id'], user_id=data['user_id'], 
                        booking_no=data['booking_no'], date=data['date'], start_time=data['start_time'],
                        end_time=data['end_time'], payment=data['payment'], status=data['status'])
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message" : "Booking Add succesfull"})


#Payment Module Are Here
class Paymentlist(Resource):

    def post(self):
        #data = request.get_json()
        data = payment_val.parse_args()
        
        payment = Payment(payment_type=data['payment_type'], booking_id=data['booking_id'],
                          user_id=data['user_id'], amount=data['amount'], date=data['date'])
        db.session.add(payment)
        db.session.commit()
        return jsonify({"message" : "Payment Add succesfull"})
