from flask import Blueprint
from flask_restful import Resource, Api, request
from .api import Users, Login, Movielist, Theaterlist, Screenlist, Bookinglist, Paymentlist, Verify


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)
api = Api(main_bp)


api.add_resource(Users, "/Register")
api.add_resource(Verify, "/verify")
api.add_resource(Login, "/login/<id>")
api.add_resource(Movielist, '/movies/<id>')
api.add_resource(Theaterlist, '/theater')
api.add_resource(Screenlist, '/screen')
api.add_resource(Bookinglist, '/booking')
api.add_resource(Paymentlist, '/payment')




