from django.shortcuts import render,redirect
from login.models import VenueManager
from booking.models import Booking,Venues
from datetime import date
from django.contrib import messages
import datetime
def dashboard(request):
  if not request.session.get('username',None):
      return redirect('manager_login')
  if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
  if request.session.get('username',None) and request.session.get('type',None)=='manager':
      username=request.session['username']
      data=VenueManager.objects.get(username=username)

      venue_data=data.venues_set.all()
      booked=venue_data.filter(is_available=False).count()
      print(booked)
      return render(request,"manager_dash/index.html",{"venue_data":venue_data,"manager":data,"booked":booked})
  else:
      return redirect("manager_login")
def add_venue(request):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.method=="GET":
        return render(request,"manager_dash/add-venue.html",{})
    else:
            venue_id=request.POST['venue_id']
            venue_type=request.POST['venue_type']
            price=request.POST['price']
            location=request.POST['location']
            venue_image=request.FILES.get('venue_image',None)
            no_of_days_advance=request.POST['no_of_days_advance']
            start_day=request.POST['start_day']
            error=[]
            if(len(venue_id)<1):
                error.append(1)
                messages.warning(request,"Venue ID Field must be atleast 3 digit like 100.")
            if(len(venue_type)<5):
                error.append(1)
                messages.warning(request,"Select a valid Venue Type.")
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter price")
            if(len(no_of_days_advance)<1):
                error.append(1)
                messages.warning(request,"Please add valid no of days a user can book venue in advance.")
            if(len(start_day)<3):
                error.append(1)
                messages.warning(request,"Please add the starting day")
            if(not len(error)):
                manager=request.session['username']
                manager=VenueManager.objects.get(username=manager)
                venue=Venues(venue_id=venue_id,location=location,venue_type=venue_type,price=price,no_of_days_advance=no_of_days_advance,start_date=datetime.datetime.strptime(start_day, "%d %B, %Y").date(),venue_image=venue_image,manager=manager)
                venue.save()
                messages.info(request,"Venue Added Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-venue/new/')
def update_venue(request,venue_id):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    venue=Venues.objects.get(venue_id=venue_id)
    if request.method=="GET":
        return render(request,"manager_dash/edit-venue.html",{"venue":venue})
    else:
            price=request.POST['price']
            no_of_days_advance=request.POST['no_of_days_advance']
            error=[]
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter correct price")
            if(len(no_of_days_advance)<1):
                error.append(1)
                messages.warning(request,"Please add valid no of days a user can book venue in advance.")
            if(not len(error)):
                manager=request.session['username']
                manager=VenueManager.objects.get(username=manager)
                venue.price=price
                venue.no_of_days_advance=no_of_days_advance
                venue.save()
                messages.info(request,"Venue Data Updated Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-venue/update/'+venue.venue_id,{"venue":venue})

