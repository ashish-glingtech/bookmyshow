from flask.views import MethodView
from flask import render_template

from models import db, Booking

class BookingList(MethodView):

    def get(self):
        booking = Booking.query.all()
        return render_template('booking.html', booking_list=booking)