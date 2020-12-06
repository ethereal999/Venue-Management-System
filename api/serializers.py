from rest_framework import serializers
from login.models import Customer
from booking.models import Booking,Venues
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','username', 'password', 'email', 'state','pin_code','address','profile_pic']
class VenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venues
        fields = ['id','manager', 'venue_id','location' 'venue_type', 'is_available','price','no_of_days_advance','start_date','venue_image']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','venue_id', 'user_id', 'start_day', 'end_day','amount','booked_on']