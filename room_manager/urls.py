from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name="manager_dashboard"),
    path('new/',views.add_venue,name="add_venue"),
    path('update/<int:venue_id>/',views.update_venue,name="update_venue"),

]
