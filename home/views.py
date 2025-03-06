from django.http import HttpResponseServerError
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from datetime import date, datetime
from home.models import DriverBookingCar
from home.models import Contact
from home.models import CarBooking
from home.models import CarServices
from home.models import MechanicService
from home.models import RentCar
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user =  form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+user)

                return redirect('login')

    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                    messages.info(request, 'Username OR password is incorrect')
                    
        context={}
        return render(request,'login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')


@login_required(login_url='login')
def manage(request):
    car =CarBooking.objects.filter(name=request.user).values()
    
    return render(request,'manage.html',{'books':car})
    



@login_required(login_url='login')
def payment(request):
    return render(request,'payment.html')

@login_required(login_url='login')
def confirm(request):
    return render(request,'confirm.html')

@login_required(login_url='login')
def services(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        model = request.POST.get('model')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        pickdate = request.POST.get('pickdate')
        pickuptime = request.POST.get('pickuptime')
        dropdate = request.POST.get('dropdate')
        droptime = request.POST.get('droptime')
        services = RentCar(name=request.user, email=email, phone=phone, destination=destination,pickdate = pickdate,pickuptime = pickuptime,dropdate=dropdate,droptime=droptime,pickup=pickup,model=model)
        services.save()
        return render(request,'payment.html')
    return render(request,'services.html')


@login_required(login_url='login')
def driverbookingcar(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        driverbookingcar = DriverBookingCar(name=name, email=email, phone=phone, destination=destination,date = date,time = time,pickup=pickup)
        driverbookingcar.save()
        return render(request,'payment.html')
   
    return render(request,'driverbookingcar.html')

@login_required(login_url='login')
def carservices(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        carservices = CarServices(name=request.user , email=email, phone=phone, destination=destination,date = date,time = time,pickup=pickup)
        carservices.save()
        return render(request,'payment.html')

    return render(request,'carservices.html')

@login_required(login_url='login')
def mechanicservices(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        mechanicservices = MechanicService(name=name, email=email, phone=phone, destination=destination,date = date,time = time)
        mechanicservices.save()
        return render(request,'payment.html')
        
    return render(request,'mechanicservices.html')

@login_required(login_url='login')
def carbooking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        model = request.POST.get('model')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        pickdate = request.POST.get('pickdate')
        pickuptime = request.POST.get('pickuptime')
        dropdate = request.POST.get('dropdate')
        droptime = request.POST.get('droptime')
        carbooking = CarBooking(name=request.user, email=email, phone=phone, destination=destination,pickdate = pickdate,pickuptime = pickuptime,dropdate=dropdate,droptime=droptime,pickup=pickup,model=model)
        carbooking.save()
        
        return render(request,'payment.html')
            
    return render(request,'carbooking.html')



@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
