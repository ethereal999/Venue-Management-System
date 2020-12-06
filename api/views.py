from rest_framework import viewsets
from login.models import Customer
from booking.models import Booking,Venues
from . import serializers

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.UserSerializer

class VenuesViewset(viewsets.ModelViewSet):
    queryset = Venues.objects.all()
    serializer_class = serializers.VenuesSerializer

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer