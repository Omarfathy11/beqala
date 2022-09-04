from dataclasses import field
from rest_framework import serializers
from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Image, Rate, Review, Resturant, CarRepair, MedicalClinic, GroceryStore


class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
    
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
    
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

      
class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturant
        fields = '__all__'


class MedicalClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalClinic
        fields = '__all__'

class CarRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRepair
        fields = '__all__'

class GroceryStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryStore
        fields = '__all__'

