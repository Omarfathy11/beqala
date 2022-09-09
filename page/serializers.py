from dataclasses import field
from rest_framework import serializers
from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Rate, Review, Resturant, CarRepair, MedicalClinic, GroceryStore
from .mixins import NestedCreateMixin, NestedUpdateMixin


class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    governorate = GovernorateSerializer(many=True)

    def create(self, validated_data):
        governorates_data = validated_data.pop('governorate')
        city = City.objects.create(**validated_data)

        for governorate in governorates_data:
            governorate, created = Governorate.objects.get_or_create(name=address['name'])
            City.governorate.add(governorate)
            return city

    class Meta:
        model = City
        fields = '__all__'
    
class AddressSerializer(serializers.ModelSerializer):

    city = CitySerializer(many=True)

    def create(self, validated_data):
        cities_data = validated_data.pop('city')
        address = Address.objects.create(**validated_data)

        for city in cities_data:
            city, created = City.objects.get_or_create(name=address['name'])
            city.address.add(city)
            return address

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

'''
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
'''

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

    address = AddressSerializer(many=True)
    
    
    
    def create(self, validated_data):
        addresses_data = validated_data.pop('address')
        restaurant = Resturant.objects.create(**validated_data)

        for address in addresses_data:
            address, created = Address.objects.get_or_create(name=address['name'])
            restaurant.address.add(address)
            return restaurant

    class Meta:
        model = Resturant
        fields = '__all__'


    
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


