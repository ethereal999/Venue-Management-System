from django.shortcuts import render,redirect
from .models import Contact
from .models import Venues,Booking
from login.models import Customer
from django.contrib import messages
from django.http import HttpResponse
import datetime
def index(request):
    return render(request,'booking/index.html',{})
def contact(request):
    if request.method=="GET":
     return render(request,"contact/contact.html",{})
    else:
     username=request.POST['name']
     email=request.POST['email']
     message=request.POST['message']
     data=Contact(name=username,email=email,message=message)
     data.save()
     return render(request,"contact/contact.html",{'message':'Thank you for contacting us.'})
def book(request):
    if request.method=="POST":
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']

        request.session['start_date']=start_date
        request.session['end_date']=end_date
        location = request.POST['location']

        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
        no_of_days=(end_date-start_date).days


        data=Venues.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date,location__contains=location)

        request.session['no_of_days']=no_of_days
        return render(request,'booking/book.html',{'data':data})
    else:
        return redirect('index')
def book_now(request,id):
    if request.session.get("username",None) and request.session.get("type",None)=='customer':
        if request.session.get("no_of_days",1):
            no_of_days=request.session['no_of_days']
            start_date=request.session['start_date']
            end_date=request.session['end_date']
            request.session['venue_id']=id
            data=Venues.objects.get(venue_id=id)
            bill=data.price*int(no_of_days)
            request.session['bill']=bill
            venueManager=data.manager.username
            return render(request,"booking/book-now.html",{"no_of_days":no_of_days,"venue_id":id,"data":data,"bill":bill,"venueManager":venueManager,"start":start_date,"end":end_date})
        else:
            return redirect("index")
    else:
        next="book-now/"+id
        return redirect('user_login')
def book_confirm(request):
    venue_id=request.session['venue_id']
    start_date=request.session['start_date']
    end_date=request.session['end_date']
    username=request.session['username']
    user_id=Customer.objects.get(username=username)
    venue=Venues.objects.get(venue_id=venue_id)
    amount=request.session['bill']
    start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
    end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
    data=Booking(venue_id=venue,start_day=start_date,end_day=end_date,amount=amount,user_id=user_id)
    data.save()
    venue.is_available=False
    venue.save()
    del request.session['start_date']
    del request.session['end_date']
    del request.session['bill']
    del request.session['venue_id']
    messages.info(request,"Venue has been successfully booked")
    return redirect('user_dashboard')
def cancel_venue(request,id):
    data=Booking.objects.get(id=id)
    venue=data.venue_id
    venue.is_available=True
    venue.save()
    data.delete()
    return HttpResponse("Booking Cancelled Successfully")
def delete_venue(request,id):
    data=Venues.objects.get(id=id)
    manager=data.manager.username
    if manager==request.session['username']:
        data.delete()
        return HttpResponse("You have deleted the Venue successfully")
    else:
        return HttpResponse("Invalid Request")


            



    
