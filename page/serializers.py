from dataclasses import field
from rest_framework import serializers

from .models import Governorate, City, Address, Phone, Social, OpeningHour, Place, Rate, Review, Resturant
from .models import CarRepair, ImageCollection
from .models import MedicalClinic, GroceryStore, ImageCollection

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.response import Response
from rest_framework import status


class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

    def create(self, validated_data):
        openingHours = OpeningHour.objects.create(
            **validated_data
        )
        return openingHours


class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    governorate = GovernorateSerializer()

    def create(self, validated_data):
        governorate_data = validated_data.pop('governorate')
        city = City.objects.create(
            governorate=Governorate.objects.create(
                **governorate_data
            )
            ** validated_data,
        )
        return city

    class Meta:
        model = City
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):

    city = CitySerializer()

    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        city_data = validated_data.pop('city')
        governorate_data = city_data.pop('governorate')
        address = Address.objects.create(
            city=City.objects.create(
                governorate=Governorate.objects.create(
                    **governorate_data
                )
                ** city_data
            ),
            **validated_data
        )
        return address


class PlaceSerializer(serializers.ModelSerializer):
    pass


class SocialSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(source='place_set')

    def create(self, validated_data):
        place_data = validated_data.pop('place_set')
        place_data = Place.objects.create(
            place=place,
            **social_data
        )
        return place

    class Meta:
        model = Social
        fields = '__all__'


class ImageCollectionSerializer(serializers.ModelSerializer):

    place = PlaceSerializer(source='place_set', read_only=True, many=True)

    class Meta:
        model = ImageCollection
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):

    place = PlaceSerializer(source='place_set', read_only=True, many=True)

    class Meta:
        model = Phone
        fields = '__all__'


class ResturantSerializer(PlaceSerializer):

    openingHour = OpeningHourSerializer()
    address = AddressSerializer()
    # social = SocialSerializer()

    class Meta:
        model = Resturant
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        
        city_data = address_data.pop('city')
        governorate_data = city_data.pop('governorate')

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
            **validated_data,
        )
        
        return resturant

    '''
    def create(self, validated_data):
        openingHour_data = validated_data.pop('openingHour')
        resturant = Resturant.objects.create(openingHour=OpeningHour.objects.create(**openingHour_data)**validated_data)

        return resturant
    '''

    # social_data = validated_data.pop('social_set')
    # social_data = Social.objects.create(
    #     resturant = resturant,
    #     **social_data
    # )


class MedicalClinicSerializer(PlaceSerializer):

    class Meta:
        model = MedicalClinic
        fields = '__all__'

   # openingHour = OpeningHourSerializer()
    address = AddressSerializer()
    # social = SocialSerializer()

    class Meta:
        model = Resturant
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        city_data = address_data.pop('city')
        governorate_data = city_data.pop('governorate')
        
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
            **validated_data,
        )

        # opening_hours = OpeningHour.objects.create(
        #     resturant = resturant,
        #     **openingHour_data
        # )

        # social_data = Social.objects.create(
        #     resturant = resturant,
        #     **social_data
        # )
        return medicalClinic


class CarRepairSerializer(PlaceSerializer):

    class Meta:
        model = CarRepair
        fields = '__all__'

    # openingHour = OpeningHourSerializer()
    address = AddressSerializer()
    # social = SocialSerializer()

    class Meta:
        model = Resturant
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        city_data = address_data.pop('city')
        governorate_data = city_data.pop('governorate')
        # openingHour_data = validated_data.pop('openingHour')

        # social_data = validated_data.pop('social_set')

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
            **validated_data,
        )

        # opening_hours = OpeningHour.objects.create(
        #     resturant = resturant,
        #     **openingHour_data
        # )

        # social_data = Social.objects.create(
        #     resturant = resturant,
        #     **social_data
        # )
        return carRepair


class GroceryStoreSerializer(PlaceSerializer):

    class Meta:
        model = GroceryStore
        fields = '__all__'

  # openingHour = OpeningHourSerializer()
    address = AddressSerializer()
    # social = SocialSerializer()

    class Meta:
        model = Resturant
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        city_data = address_data.pop('city')
        governorate_data = city_data.pop('governorate')
        # openingHour_data = validated_data.pop('openingHour')

        # social_data = validated_data.pop('social_set')

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
            **validated_data,
        )

        # opening_hours = OpeningHour.objects.create(
        #     resturant = resturant,
        #     **openingHour_data
        # )

        # social_data = Social.objects.create(
        #     resturant = resturant,
        #     **social_data
        # )
        return groceryStore

# class RateSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Rate
#         fields = '__all__'


# class ReviewSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'
