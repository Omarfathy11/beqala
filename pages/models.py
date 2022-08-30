from django.db import models
from user.models import User


class Address(models.Model):
    governorate = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    street = models.CharField(30)


class Place(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(blank=False, unique=True)
    description = models.TextField(max_length=800)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    openingHours = models.TextField()


class Review(models.Model):
    review = models.TextField(max_length=1000)
    reviewer = models.ForeignKey(User)
    reviewer = models.ForeignKey(Place)
    date = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    rate = models.IntegerField(max_length=5)
    ratedTo = models.ForeignKey(Place)



class Resturant(Place):
    pass


class MedicalClinic(Place):
    pass


class Cafe(Place):
    pass

class CarRepair(Place):
    pass


class GroceryStore(Place):
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

