from flask_restful import reqparse

#movies Add Validation Api
parser = reqparse.RequestParser()
parser.add_argument('name', type = str, required=True, help="enter a valid name")
parser.add_argument('descr', type = str, required=True, help="enter a valid descrtion")
parser.add_argument('duration', type = str, required=True, help="enter a valid duration")
parser.add_argument('language', type = str, required=True, help="enter a valid language")
parser.add_argument('movie_type', type = str, required=True, help="enter a valid movie type")
parser.add_argument('image', type = str, required=True, help="enter a valid image")


#theater Add Validation Api
theater1 = reqparse.RequestParser()
theater1.add_argument('name', type = str, required=True, help="enter a valid name")
theater1.add_argument('location', type = str, required=True, help="enter a valid location")
theater1.add_argument('rating', type = str, required=True, help="enter a valid rating")
theater1.add_argument('phone_no', type = int, required=True, help="enter a valid phone_no")


#Screen Add Validation Api
screen_val = reqparse.RequestParser()
screen_val.add_argument('name', type = str, required=True, help="Enter a valid Name")
screen_val.add_argument('movie_id', type = str, required=True, help="Enter a valid movie Id")
screen_val.add_argument('theater_id', type = str, required=True, help="Enter a valid theater Id")
screen_val.add_argument('ticket_type', type = str, required=True, help="Enter a valid Ticket Type")
screen_val.add_argument('total_seats', type = int, required=True, help="Enter a valid Total Seats")


#Booking Add Validation Api
booking_val = reqparse.RequestParser()
booking_val.add_argument('screen_id', type = str, required=True, help="Enter a valid Screen Id")
booking_val.add_argument('user_id', type = int, required=True, help="Enter a valid user Id")
booking_val.add_argument('booking_no', type = str, required=True, help="Enter a valid Booking no")
booking_val.add_argument('date', type = str, required=True, help="Enter a valid Date")
booking_val.add_argument('start_time', type = str, required=True, help="Enter a valid Start Time")
booking_val.add_argument('end_time', type = str, required=True, help="Enter a valid End Time")
booking_val.add_argument('payment', type = str, required=True, help="Enter a valid payment")
booking_val.add_argument('status', type = str, required=True, help="Enter a valid status")


#payment Add Validation Api
payment_val = reqparse.RequestParser()
payment_val.add_argument('payment_type', type = str, required=True, help="Enter a valid Screen Id")
payment_val.add_argument('booking_id', type = int, required=True, help="Enter a valid Booking Id")
payment_val.add_argument('user_id', type = str, required=True, help="Enter a valid User Id")
payment_val.add_argument('amount', type = str, required=True, help="Enter a valid Amount")
payment_val.add_argument('date', type = str, required=True, help="Enter a valid Date")
