from django.contrib import admin
from django.urls import path,include 
from home import views


urlpatterns = [

    path("register",views.registerPage,name='regsiter'),

    path("login",views.loginPage,name='login'),
    
    path("logout",views.logoutUser,name='logout'), 
    
    path("",views.index,name='home'),
    
    path("about",views.about,name='about'),
    
    path("services",views.services,name='services'),

    path("driverbookingcar",views.driverbookingcar,name='driverbookingcar'),

    path("carservices",views.carservices,name='carservices'),

    path("mechanicservices",views.mechanicservices,name='mechanicservices'),

    path("carbooking",views.carbooking,name='carbooking'),
    
    path("confirm",views.confirm,name='confirm'),

    path("payment",views.payment,name='payment'),

    path("contact",views.contact,name='contact'),

    path("manage",views.manage,name='manage'),

    
   
    
]