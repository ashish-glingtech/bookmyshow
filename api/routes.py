from flask import Blueprint
from flask_restful import Resource, Api, request
from .api import Users, Login, TheaterStore, TheaterList, MovieStore, MovieList, ScreenStore, ScreenList, BookingStore ,BookingList,  PaymentList, PaymentStore, Image, ActorStore, ActorList, CrewStore, CrewList, OtpSave, OtpVerify,OtpReset


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)
api = Api(main_bp)


api.add_resource(Users, "/register")
#api.add_resource(Verify, "/verify")
api.add_resource(Login, "/login/<id>")
api.add_resource(MovieStore, '/movies')
api.add_resource(MovieList, '/movies/<id>')
api.add_resource(Image, "/image/")
api.add_resource(TheaterStore, '/theater')
api.add_resource(TheaterList, '/theater/<id>')
api.add_resource(ScreenStore, '/screen')
api.add_resource(ScreenList, '/screen/<id>')
api.add_resource(BookingStore, '/booking')
api.add_resource(BookingList, '/booking/<id>')
api.add_resource(PaymentStore, '/payment')
api.add_resource(PaymentList, '/payment/<id>')
api.add_resource(ActorStore, '/actor')
api.add_resource(ActorList, '/actor/<id>')
api.add_resource(CrewStore, '/crew')
api.add_resource(CrewList, '/crew/<id>')
api.add_resource(OtpSave, '/otp')
api.add_resource(OtpVerify, '/otpverify')
api.add_resource(OtpReset, '/reset')




#O9mQx4BVtGr7WZue0vfsha9wfHD__ALqGjPWTtJ1 data from twilo