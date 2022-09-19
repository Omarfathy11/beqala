from dataclasses import field
from rest_framework import serializers

from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Rate, Review, Resturant
from .models import CarRepair, ImageCollection
from .models import MedicalClinic, GroceryStore, ImageCollection

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.response import Response


class OpeningHourSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

    def create(self, validated_data):
        openingHours = OpeningHour.objects.create(**validated_data)
        return openingHours


class GovernorateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = '__all__'


class CitySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    governorate = GovernorateSerializer()

    # def create(self, validated_data):
    #     governorate_data = validated_data.pop('governorate')
    #     city = City.objects.create(
    #         governorate=Governorate.objects.create(
    #             **governorate_data
    #         )
    #         ** validated_data,
    #     )

    #     return city


    class Meta:
        model = City
        fields = '__all__'


class AddressSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    city = CitySerializer()

    class Meta:
        model = Address
        fields = '__all__'

    # def create(self, validated_data):
    #     city_data = validated_data.pop('city')
    #     governorate_data = city_data.pop('governorate')
    #     address = Address.objects.create(
    #         city=City.objects.create(
    #             governorate=Governorate.objects.create(
    #                 **governorate_data
    #             )
    #             ** city_data
    #         ),
    #         **validated_data
    #     )

    #     return address


class PlaceSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    pass


class SocialSerializer(WritableNestedModelSerializer, serializers.ModelSerializer, ):

    def create(self, validated_data):
        social = Social.objects.create(**validated_data)
        return social

    class Meta:
        model = Social
        fields = '__all__'


class ImageCollectionSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    place = PlaceSerializer(source='place_set', read_only=True, many=True)

    class Meta:
        model = ImageCollection
        fields = '__all__'


class PhoneSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    place = PlaceSerializer(source='place_set', read_only=True, many=True)

    def create(self, validated_data):
        phone = Phone.objects.create(**validated_data)
        return phone


    class Meta:
        model = Phone
        fields = '__all__'


class ResturantSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    phone = PhoneSerializer(source='phone_set', many=True)

    openingHours = OpeningHourSerializer()
    
    address = AddressSerializer()

    social = SocialSerializer()

    image = ImageCollectionSerializer(source='imagecollection_set', many=False, required=False) 

    class Meta:
        model = Resturant
        fields = '__all__'

    def create(self, validated_data):
        
        address_data = validated_data.pop('address')
        
        city_data = address_data.pop('city')

        governorate_data = city_data.pop('governorate')

        openingHours_data = validated_data.pop('openingHours')

        phone_data = validated_data.pop('phone_set')

        social_data = validated_data.pop('social')

        #image_data = validated_data.pop('imagecollection_set')
        
        resturant = Resturant.objects.create(

            address=Address.objects.create(
                city=City.objects.create(
                    governorate=Governorate.objects.create(
                        **governorate_data
                    ), 
                    **city_data
                ), 
                **address_data
            ),

            openingHours=OpeningHour.objects.create(**openingHours_data),

            social = Social.objects.create(**social_data),

            #image = ImageCollection.objects.create(**image_data),

            **validated_data,
        )

        for phone in phone_data:
            phone = Phone.objects.create(
                place_id=resturant.id,
                **phone
            )

        return resturant
        
       
class MedicalClinicSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    openingHours = OpeningHourSerializer()
    
    address = AddressSerializer()

    phone = PhoneSerializer(source='phone_set', many=True)

    social = SocialSerializer()

    

    class Meta:
        model = MedicalClinic
        fields = '__all__'


    def create(self, validated_data):
        
        address_data = validated_data.pop('address')
        
        city_data = address_data.pop('city')
    
        governorate_data = city_data.pop('governorate')

        openingHours_data = validated_data.pop('openingHours')

        phone_data = validated_data.pop('phone_set')

        social_data = validated_data.pop('social')
        
        #image_data = validated_data.pop('imagecollection_set')

        medicalClinic = MedicalClinic.objects.create(
            address=Address.objects.create(
                city=City.objects.create(
                    governorate=Governorate.objects.create(
                        **governorate_data
                    ), 
                    **city_data
                ), 
                **address_data
            ),
            openingHours=OpeningHour.objects.create(**openingHours_data),

            #phone = Phone.objects.create(**phone_data),

            social = Social.objects.create(**social_data),

            **validated_data,
        )
         
        for phone in phone_data:
            phone = Phone.objects.create(
                place_id=medicalClinic.id,
                **phone
            )

        # for image in image_data:
        #     image = ImageCollection.objects.create(
        #         place_id=resturant.id,
        #         **image
        #     )

        return medicalClinic


class CarRepairSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    openingHours = OpeningHourSerializer()
    
    address = AddressSerializer()

    phone = PhoneSerializer(source='phone_set', many=True)

    social = SocialSerializer()

    class Meta:
        model = CarRepair
        fields = '__all__'

    def create(self, validated_data):
        
        address_data = validated_data.pop('address')
        
        city_data = address_data.pop('city')
    
        governorate_data = city_data.pop('governorate')

        openingHours_data = validated_data.pop('openingHours')

        phone_data = validated_data.pop('phone_set')

        social_data = validated_data.pop('social')

        #image_data = validated_data.pop('imagecollection_set')
        
        carRepair = CarRepair.objects.create(
            address=Address.objects.create(
                city=City.objects.create(
                    governorate=Governorate.objects.create(
                        **governorate_data
                    ), 
                    **city_data
                ), 
                **address_data
            ),
            openingHours=OpeningHour.objects.create(**openingHours_data),

            #phone = Phone.objects.create(**phone_data),

            social = Social.objects.create(**social_data),

            **validated_data,
        )

        for phone in phone_data:
            phone = Phone.objects.create(
                place_id=carRepair.id,
                **phone
            )

        # for image in image_data:
        #     image = ImageCollection.objects.create(
        #         place_id=resturant.id,
        #         **image
        #     )

        return carRepair


class GroceryStoreSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    openingHours = OpeningHourSerializer()
    
    address = AddressSerializer()

    phone = PhoneSerializer(source='phone_set', many=True)

    social = SocialSerializer()

    class Meta:
        model = GroceryStore
        fields = '__all__'



    def create(self, validated_data):
        
        address_data = validated_data.pop('address')
        
        city_data = address_data.pop('city')
    
        governorate_data = city_data.pop('governorate')

        openingHours_data = validated_data.pop('openingHours')

        phone_data = validated_data.pop('phone_set')
        
        social_data = validated_data.pop('social')

        #image_data = validated_data.pop('imagecollection_set')
        
        groceryStore = GroceryStore.objects.create(
            address=Address.objects.create(
                city=City.objects.create(
                    governorate=Governorate.objects.create(
                        **governorate_data
                    ), 
                    **city_data
                ), 
                **address_data
            ),
            openingHours=OpeningHour.objects.create(**openingHours_data),
            #phone = Phone.objects.create(**phone_data),
            social = Social.objects.create(**social_data),
            
            **validated_data,
        )

        for phone in phone_data:
            phone = Phone.objects.create(
                place_id=groceryStore.id,
                **phone
            )
        

        return groceryStore

# class RateSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Rate
#         fields = '__all__'


# class ReviewSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'
