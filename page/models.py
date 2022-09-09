from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField



class Governorate(models.Model):
    Governorate_Name = models.CharField(max_length=30)
    zipCode = models.IntegerField(null=False)


class City(models.Model):
    City_name = models.CharField(max_length=30, null=True)
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE, null=True)

class Address(models.Model):
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=30, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)



class Phone(models.Model):
    phone1 = models.CharField(primary_key=True, max_length=15, null=False)
    phone2 = models.CharField(primary_key=False, max_length=15, null=True)
    phone3 = models.CharField(primary_key=False, max_length=15, null=True)


class Social(models.Model):
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)

class OpeningHour(models.Model):
    open_from = models.TimeField()
    open_to = models.TimeField()
    from_Day = models.CharField(max_length=10)
    to_Day = models.CharField(max_length=10)

#CATEGORISED
# place = [('Restaurant', 'Restaurant'), ('Cafe', 'Cafe'), ('MedicalClinic', 'Medical Clinic'), ('CarRepair', 'Car Repair'), ('GroceryStore', 'Grocery store')]
 
class Place(models.Model):
    Place_Name = models.CharField(max_length=100)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    description = models.TextField(max_length=800)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    openingHours = models.ForeignKey(OpeningHour, on_delete=models.CASCADE)
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    cover = models.ImageField(null=True)
    photosCollection = ArrayField(
        ArrayField(
            models.ImageField(blank=True),
            size=10,
        ),null=True,
        size=10,
        )

    
    def __str__(self):
        return self.name

'''   
class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    Image = ArrayField(
        ArrayField(
            models.ImageField(blank=True),
            size=10,
        ),
        size=10,
        )
    
'''    

class Review(models.Model):
    review = models.TextField(max_length=1000, null=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    rate = models.IntegerField()
    ratedTo = models.ForeignKey(Place, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])



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
