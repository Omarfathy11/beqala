from django.contrib import admin
from .models import Place, Resturant, MedicalClinic, CarRepair, GroceryStore, Governorate, City, Address, Phone, Social, OpeningHour

''', Cafe, Hotel, Backers, ATM, Gym, PlayGrounds'''


# Register your models here.
class ResturantAdmin(admin.ModelAdmin):
    list_display = ['id', 'dishes', 'atmosphere']
    list_filter = ['dishes', 'atmosphere']
    search_fields = ['dishes', 'atmosphere']

class PlaceAdmin(admin.ModelAdmin):
     list_display = ['id', 'Place_Name', 'phone', 'description', 'address', 'openingHours', 'social', 'cover',]
     list_filter = ['Place_Name', 'phone', 'description', 'address', 'openingHours', 'social', 'cover']
     search_fields = ['name', 'phone', 'description', 'address', 'openingHours', 'social', 'cover']

admin.site.register(Place, PlaceAdmin)
admin.site.register(Resturant, ResturantAdmin)
admin.site.register(MedicalClinic)
admin.site.register(CarRepair)
admin.site.register(GroceryStore)
admin.site.register(Phone)
admin.site.register(City)
admin.site.register(OpeningHour)
admin.site.register(Address)
admin.site.register(Social)
#admin.site.register(Image)
admin.site.register(Governorate)