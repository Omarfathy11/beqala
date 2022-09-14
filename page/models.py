from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField



class Governorate(models.Model):
    Governorate_Name = models.CharField(max_length=30)
    zipCode = models.IntegerField(null=False)


class City(models.Model):
    City_name = models.CharField(max_length=30, null=True)
    governorate = models.ForeignKey(Governorate, on_delete=models.SET_NULL, null=True)

class Address(models.Model):
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=30, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)



class Phone(models.Model):
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=15, null=False)


class Social(models.Model):
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)

class OpeningHour(models.Model):
    open_from = models.TimeField(auto_now_add=True)
    open_to = models.TimeField(auto_now_add=True)
    from_Day = models.CharField(max_length=10)
    to_Day = models.CharField(max_length=10)

    

class ImageCollection(models.Model):
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True)
    is_default = models.BooleanField(default=False)

    
class Place(models.Model):
    Place_Name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=800, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    openingHours = models.ForeignKey(OpeningHour, on_delete=models.SET_NULL, null=True)
    social = models.ForeignKey(Social, on_delete=models.SET_NULL, null=True)

    

class Resturant(Place):
    dishes = models.CharField(max_length=100, null=True)
    atmosphere = models.CharField(max_length=30, null=True)
   # languageSpoken = models.CharField(max_length=30)
   # features = models.CharField(max_length=100)


class MedicalClinic(Place):
    products = models.TextField(max_length=200)
    #languageSpoken = models.CharField(max_length=30)
    brands = models.CharField(max_length=40)
    
    #specialties = models.TextField(max_length=100)


class CarRepair(Place):
     products = models.TextField(max_length=200)
     #languageSpoken = models.CharField(max_length=30)
     brands = models.CharField(max_length=40)
     #specialties = models.TextField(max_length=100)



class GroceryStore(Place):
     brands = models.CharField(max_length=40)
     #languageSpoken = models.CharField(max_length=30)

     
class Review(models.Model):
    review = models.TextField(max_length=1000, null=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    rate = models.IntegerField()
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    stars = models.IntegerField()



class Cafe(Place):
    pass

class Hotel(Place):
    pass

class Backers(Place):
    pass

class ATM(Place):
    pass

class Gym(Place):
    pass

class PlayGrounds(Place):
    pass




