from dataclasses import field
from rest_framework import serializers
from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Rate, Review, Resturant, CarRepair, MedicalClinic, GroceryStore, Image, ImageCollection
from drf_writable_nested import WritableNestedModelSerializer


class PhoneSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
   
    class Meta:
        model = Phone
        fields = '__all__'

class SocialSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

class OpeningHourSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

class RateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class ReviewSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class GovernorateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = ['Governorate_Name', 'zipCode']

class CitySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    governorate = GovernorateSerializer()

    
    class Meta:
        model = City
        fields = ['City_name', 'governorate']
    
class AddressSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    city = CitySerializer()

    
    class Meta:
        model = Address
        fields = ['line1', 'line2', 'city']
        depth = 4


class ImageCollectionSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = ImageCollection
        fields = ['place_collection']

class ImageSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    collection = ImageCollectionSerializer()

    class Meta:
        model = Image
        fields = ['cover', 'collection']



class PlaceSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    phone = PhoneSerializer()
    openingHours = OpeningHourSerializer()
    social = SocialSerializer()

    image = ImageSerializer()
    address = AddressSerializer()

    class Meta:
        model = Place
        fields = ['Place_Name', 'description', 'address', 'openingHours', 'phone', 'image', 'social']



      
class ResturantSerializer(PlaceSerializer):

    place = PlaceSerializer()
    
    class Meta:
        model = Resturant
        fields = ['place', 'dishes', 'atmosphere']
        depth = 4


    
class MedicalClinicSerializer(PlaceSerializer):
    place = PlaceSerializer()


    class Meta:
        model = MedicalClinic
        fields = ['place', 'products', 'brands']
        depth = 4

class CarRepairSerializer(PlaceSerializer):
    place = PlaceSerializer()
    
    class Meta:
        model = CarRepair
        fields = ['place', 'products', 'brands']
        depth = 4

class GroceryStoreSerializer(PlaceSerializer):
    place = PlaceSerializer()

    class Meta:
        model = GroceryStore
        fields = ['place', 'products', 'brands']
        depth = 4


