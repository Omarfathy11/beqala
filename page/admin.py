from django.contrib import admin
from .models import Place, Resturant, MedicalClinic, CarRepair, GroceryStore 

''', Cafe, Hotel, Backers, ATM, Gym, PlayGrounds'''


# Register your models here.

admin.site.register(Resturant)
admin.site.register(MedicalClinic)
admin.site.register(CarRepair)
admin.site.register(GroceryStore)