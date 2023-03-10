from flask_restful import reqparse
import werkzeug


#user Add Validation Api
user_val=reqparse.RequestParser()
user_val.add_argument('name', type=str, required=True, help="Enter a valid Name", location='form')
user_val.add_argument('gender', type=str, required=True, help="Enter a valid Gender",location='form')
user_val.add_argument('age', type=int, required=True, help="Enter a valid Age", location='form')
user_val.add_argument('email', type=str, required=True, help="Enter a valid Email", location='form')
user_val.add_argument('password', type=str, required=True, help="Enter a valid Password", location='form')
user_val.add_argument('phone_no', type=int, required=True, help="Enter a valid Phone no", location='form')


#movies Add Validation Api
parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=False, help="Enter a valid Number", location='form')
parser.add_argument('name', type=str, required=True, help="Enter a valid Name", location='form')
parser.add_argument('descr', type=str, required=True, help="Enter a valid Descrtion", location='form')
parser.add_argument('duration', type=str, required=True, help="Enter a valid Duration", location='form')
parser.add_argument('language', type=str, required=True, help="Enter a valid Language", location='form')
parser.add_argument('movie_type', type=str, required=True, help="Enter a valid Movie Type", location='form')
parser.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True, help="Enter a valid Image", location='files')


#theater Add Validation Api
theater1 = reqparse.RequestParser()
theater1.add_argument('name', type=str, required=True, help="Enter a valid Name", location='form')
theater1.add_argument('location', type=str, required=True, help="Enter a valid Location",location='form')
theater1.add_argument('rating', type=str, required=True, help="Enter a valid Rating", location='form')
theater1.add_argument('phone_no', type=int, required=True, help="Enter a valid Phone No", location='form')


#Screen Add Validation Api
screen_val = reqparse.RequestParser()
screen_val.add_argument('name', type=str, required=True, help="Enter a valid Name", location='form')
screen_val.add_argument('movie_id', type=str, required=True, help="Enter a valid movie Id", location='form')
screen_val.add_argument('theater_id', type=str, required=True, help="Enter a valid theater Id", location='form')
screen_val.add_argument('ticket_type', type=str, required=True, help="Enter a valid Ticket Type", location='form')
screen_val.add_argument('total_seats', type=int, required=True, help="Enter a valid Total Seats", location='form')


#Booking Add Validation Api
booking_val = reqparse.RequestParser()
booking_val.add_argument('screen_id', type=int, required=True, help="Enter a valid Screen Id", location='form')
booking_val.add_argument('user_id', type=int, required=True, help="Enter a valid user Id", location='form')
booking_val.add_argument('booking_no', type=str, required=True, help="Enter a valid Booking no", location='form')
booking_val.add_argument('date', type=str, required=True, help="Enter a valid Date", location='form')
booking_val.add_argument('start_time', type=str, required=True, help="Enter a valid Start Time", location='form')
booking_val.add_argument('end_time', type=str, required=True, help="Enter a valid End Time", location='form')
booking_val.add_argument('payment', type=str, required=True, help="Enter a valid payment", location='form')
booking_val.add_argument('status', type=str, required=True, help="Enter a valid status", location='form')


#payment Add Validation Api
payment_val = reqparse.RequestParser()
payment_val.add_argument('payment_type', type=str, required=True, help="Enter a valid Screen Id", location='form')
payment_val.add_argument('booking_id', type=int, required=True, help="Enter a valid Booking Id", location='form')
payment_val.add_argument('user_id', type=str, required=True, help="Enter a valid User Id", location='form')
payment_val.add_argument('amount', type=str, required=True, help="Enter a valid Amount", location='form')
payment_val.add_argument('date', type=str, required=True, help="Enter a valid Date", location='form')


#Actor Add Validation Api
actor_val = reqparse.RequestParser()
actor_val.add_argument('name', type=str, required=True, help="Enter a valid Name", location='form')
actor_val.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True, help="Enter a valid Image ", location='files')
actor_val.add_argument('actor_type', type=str, required=True, help="Enter a valid Actor Type", location='form')
actor_val.add_argument('movie_id', type=str, required=True, help="Enter a valid Movie Id", location='form')


#Crew Add Validation Api
crew_val = reqparse.RequestParser()
crew_val.add_argument('name', type=str, required=True, help="Enter a valid Name", location='form')
crew_val.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True, help="Enter a valid Image ", location='files')
crew_val.add_argument('crew_type', type=str, required=True, help="Enter a valid Crew Type", location='form') 
crew_val.add_argument('movie_id', type=str, required=True, help="Enter a valid Movie Id", location='form')


#Otp Add Validation Api
otp_val = reqparse.RequestParser()
otp_val.add_argument('otp_id', type=int, required=False, help="Number  not  found", location='form')
otp_val.add_argument('phone_number', type=int, required=True, help="Enter a valid Number", location='form')
