from dataclasses import field
from rest_framework import serializers
from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Rate, Review, Resturant, CarRepair, MedicalClinic, GroceryStore, ImageCollection
from drf_writable_nested import WritableNestedModelSerializer


class PhoneSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Phone
        fields = '__all__'
    
    def create(self, validated_data):
        print('Create')
        return super().create(validated_data)

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

# class RateSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Rate
#         fields = '__all__'


# class ReviewSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'


class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = '__all__'

class CitySerializer(WritableNestedModelSerializer):

    governorate = GovernorateSerializer()

    class Meta:
        model = City
        fields = '__all__'
    
class AddressSerializer(WritableNestedModelSerializer):

    city = CitySerializer()

    
    class Meta:
        model = Address
        fields = '__all__'


class ImageCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCollection
        fields = '__all__'



class PlaceSerializer(serializers.ModelSerializer):

    address = AddressSerializer()
    openingHours = OpeningHourSerializer()
    social = SocialSerializer()

    phone = PhoneSerializer(source='phone_set')
    image = ImageCollectionSerializer(source='imagecollection_set', allow_null=True, read_only=True)


      
class ResturantSerializer(PlaceSerializer):

    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Resturant
        fields = '__all__'


    
# class MedicalClinicSerializer(PlaceSerializer):
#     place = PlaceSerializer()


#     class Meta:
#         model = MedicalClinic
#         fields = ['place', 'products', 'brands']
#         depth = 4

# class CarRepairSerializer(PlaceSerializer):
#     place = PlaceSerializer()
    
#     class Meta:
#         model = CarRepair
#         fields = ['place', 'products', 'brands']
#         depth = 4

# class GroceryStoreSerializer(PlaceSerializer):
#     place = PlaceSerializer()

#     class Meta:
#         model = GroceryStore
#         fields = ['place', 'products', 'brands']
#         depth = 4


