from django.contrib import admin
from login.models import Customer, VenueManager
from booking.models import Contact,Venues,Booking
# Register your models here.
admin.site.register(Customer)
admin.site.register(VenueManager)
admin.site.register(Contact)
admin.site.register(Venues)
admin.site.register(Booking)