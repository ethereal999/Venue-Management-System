from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('book',views.book,name='book'),
    path('contact-us',views.contact,name='contact-us'),
    path('book-now/<str:id>',views.book_now,name='book-now'),
    path('cancel-venue/<str:id>',views.cancel_venue,name='cancel-venue'),
    path('delete-venue/<str:id>',views.delete_venue,name='delete-venue'),
    path('confirm-now-booking',views.book_confirm,name="book_confirm")

]