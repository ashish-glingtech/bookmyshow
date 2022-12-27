from flask import Blueprint
from flask_restful import Resource, Api, request
from .views import Users, Movie_list, Theater_list, Screen_list, Booking_list, PaymentList
# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)
api = Api(main_bp)


api.add_resource(Users, "/login")
api.add_resource(Movie_list, '/movies')
api.add_resource(Theater_list, '/theater')
api.add_resource(Screen_list, '/screen')
api.add_resource(Booking_list, '/booking')
api.add_resource(PaymentList, '/payment')




