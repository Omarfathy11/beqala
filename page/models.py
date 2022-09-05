from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField



class Governorate(models.Model):
    name = models.CharField(max_length=30)
    zipCode = models.IntegerField(max_length=6)

class City(models.Model):
    name = models.CharField(max_length=30)
    governorate = models.ForeignKey(Governorate)

class Address(models.Model):
    line1 = models.CharField(30)
    line2 = models.CharField(30)
    city = models.ForeignKey(City)




class Phone(models.Model):
    phone1 = models.CharField(primary_key=True)
    phone2 = models.CharField(primary_key=False)
    phone2 = models.CharField(primary_key=False)
    


class Social(models.Model):
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

class OpeningHour(models.Model):
    openfrom = models.TimeField()
    opento = models.TimeField()
    fromDay = models.CharField(max_length=10)
    toDay = models.CharField(max_length=10)


    
class Place(models.Model):
    name = models.CharField(max_length=100)
    phone = models.ForeignKey(Phone, unique=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=800)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    openingHours = models.ForeignKey(OpeningHour, on_delete=models.CASCADE)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    cover = models.ImageField()
    
   
class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    Image = models.ImageField()


class Review(models.Model):
    review = models.TextField(max_length=1000)
    reviewer = models.ForeignKey(User)
    reviewer = models.ForeignKey(Place)
    date = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    rate = models.IntegerField(max_length=5)
    ratedTo = models.ForeignKey(Place)



class Resturant(Place):
    dishes = models.CharField(max_length=100)
    atmosphere = models.CharField(max_length=30)
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

'''
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

'''
