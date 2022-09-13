from dataclasses import field
from rest_framework import serializers

from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Rate, Review, Resturant, CarRepair, ImageCollection
from .models import MedicalClinic, GroceryStore, ImageCollection

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_meets_djongo.serializers import DjongoModelSerializer



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


class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    governorate = GovernorateSerializer()


    # def create(self, validated_data):
    #     address_data = validated_data.pop('governorate')
    #     Resturant.objects.create(
    #         **validated_data
    #     )
    #     print(validated_data)
    #     return City

    class Meta:
        model = City
        fields = '__all__'
    
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

    city = CitySerializer()


    '''
    def create(self, validated_data):
        address_data = validated_data.pop('city')
        Resturant.objects.create(
            **validated_data
        )
        return Address
    '''


class ImageCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageCollection
        fields = '__all__'

    # def create(self, validated_data):
    #     place_data = validated_data.pop('place')
    #     ImageCollection.objects.create(
    #         **validated_data
    #     )
    #     return ImageCollection
    



class PlaceSerializer(serializers.ModelSerializer):

    #imageCollection = ImageCollectionSerializer(source='imagecollection_set', allow_null=True, read_only=True, many=True, required=False)
    #phone = PhoneSerializer(source='phone_set', many=True, read_only=True, allow_null=True)

    address = AddressSerializer()

    openingHours = OpeningHourSerializer()

    social = SocialSerializer()
    
    phone = PhoneSerializer(source='phone_set')
    


      
class ResturantSerializer(PlaceSerializer):

    class Meta:
        model = Resturant
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        openingHours_data = validated_data.pop('openingHours')
        social_data = validated_data.pop('social')
        phones_data = validated_data.pop('phone')
        
        for phone_data in phones_data:
            Resturant.objects.create(phone=phone, **validated_data)

        resturant = Resturant.objects.create(**validated_data)
        
        return resturant
    
class MedicalClinicSerializer(PlaceSerializer):

    class Meta:
        model = MedicalClinic
        fields = '__all__'

    '''
    def create(self, validated_data):
        address_data = validated_data.pop('Address')
        openingHours_data = validated_data.pop('openingHours')
        social_data = validated_data.pop('social')
        phone_data = validated_data.pop('phone')
        Resturant.objects.create(
            **validated_data
        )
        print(validated_data)
        return Resturant
    '''

class CarRepairSerializer(PlaceSerializer):
    
    class Meta:
        model = CarRepair
        fields = '__all__'
    
    '''
    def create(self, validated_data):
        address_data = validated_data.pop('Address')
        openingHours_data = validated_data.pop('openingHours')
        social_data = validated_data.pop('social')
        phone_data = validated_data.pop('phone')
        Resturant.objects.create(
            **validated_data
        )
        print(validated_data)
        return Resturant
    '''

class GroceryStoreSerializer(PlaceSerializer):

    class Meta:
        model = GroceryStore
        fields = '__all__'
    
    '''
    def create(self, validated_data):
        address_data = validated_data.pop('Address')
        openingHours_data = validated_data.pop('openingHours')
        social_data = validated_data.pop('social')
        phone_data = validated_data.pop('phone')
        Resturant.objects.create(
            **validated_data
        )
        print(validated_data)
        return Resturant
    '''

# class RateSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Rate
#         fields = '__all__'


# class ReviewSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'


