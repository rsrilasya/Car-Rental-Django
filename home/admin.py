from django.contrib import admin
from home.models import CarServices
from home.models import MechanicService
from home.models import Contact
from home.models import DriverBookingCar
from home.models import CarBooking
from home.models import RentCar
# Register your models here.
admin.site.register(Contact)
admin.site.register(MechanicService)
admin.site.register(CarServices)
admin.site.register(DriverBookingCar)
admin.site.register(CarBooking)
admin.site.register(RentCar)


