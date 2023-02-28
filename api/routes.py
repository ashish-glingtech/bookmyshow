from flask import Blueprint
from flask_restful import Resource, Api, request
from .api import Users, Login, Movielist, Theaterlist, Screenlist, Bookinglist, Paymentlist, Image, Actorlist, Crewlist, Otplist, Otpverify,Otprest


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)
api = Api(main_bp)


api.add_resource(Users, "/Register")
#api.add_resource(Verify, "/verify")
api.add_resource(Login, "/login/")
api.add_resource(Movielist, '/movies/<id>')
api.add_resource(Image, "/image/")
api.add_resource(Theaterlist, '/theater/<id>')
api.add_resource(Screenlist, '/screen/<id>')
api.add_resource(Bookinglist, '/booking/<id>')
api.add_resource(Paymentlist, '/payment/<id>')
api.add_resource(Actorlist, '/actor/')
api.add_resource(Crewlist, '/crew/')
api.add_resource(Otplist, '/otp/')
api.add_resource(Otpverify, '/otpverify/')
api.add_resource(Otprest, '/reset')




#O9mQx4BVtGr7WZue0vfsha9wfHD__ALqGjPWTtJ1 data from twilo