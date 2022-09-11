from dataclasses import field
from rest_framework import serializers
from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Rate, Review, Resturant, CarRepair, MedicalClinic, GroceryStore, Image
from .mixins import NestedCreateMixin, NestedUpdateMixin


class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = ['Governorate_Name', 'zipCode']

class CitySerializer(serializers.ModelSerializer):

    governorate = GovernorateSerializer()

    
    class Meta:
        model = City
        fields = ['City_name', 'governorate']
    
class AddressSerializer(serializers.ModelSerializer):

    city = CitySerializer()

    
    class Meta:
        model = Address
        #fields = '__all__'
        fields = ['line1', 'line2', 'city']
        depth = 4




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
        #fields = '__all__'
        fields = ['cover', 'photosCollection']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

      
class ResturantSerializer(NestedCreateMixin, NestedUpdateMixin, serializers.ModelSerializer):
    phone = PhoneSerializer()
    openingHours = OpeningHourSerializer()
    social = SocialSerializer()

    image = ImageSerializer()

    address = AddressSerializer()
    
    class Meta:
        model = Resturant
        #fields = '__all__'
        fields = ['Place_Name', 'description', 'openingHours', 'social', 'address', 'phone', 'image']
        depth = 4


    
class MedicalClinicSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()
    openingHours = OpeningHourSerializer()
    social = SocialSerializer()
    address = AddressSerializer()
    city = CitySerializer()
    governorate = GovernorateSerializer()

    class Meta:
        model = MedicalClinic
        fields = '__all__'
        depth = 4

class CarRepairSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    openingHours = OpeningHourSerializer()
    social = SocialSerializer()
    address = AddressSerializer()
    city = CitySerializer()
    governorate = GovernorateSerializer()
    
    class Meta:
        model = CarRepair
        fields = '__all__'
        depth = 4

class GroceryStoreSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()
    openingHours = OpeningHourSerializer()
    social = SocialSerializer()
    address = AddressSerializer()
    city = CitySerializer()
    governorate = GovernorateSerializer()
    class Meta:
        model = GroceryStore
        fields = '__all__'
        depth = 4


