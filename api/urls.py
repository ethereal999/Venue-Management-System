from django.urls import path,include
from rest_framework import routers
from . import views
router=routers.DefaultRouter()
router.register(r'customer', views.CustomerViewset)
router.register(r'booking', views.BookingViewset)
router.register(r'venues', views.VenuesViewset)
urlpatterns = [
    path('',include(router.urls))
]
