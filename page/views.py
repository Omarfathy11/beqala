from django.shortcuts import render
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from .serializers import GovernorateSerializer, CitySerializer, AddressSerializer, PhoneSerializer, SocialSerializer, OpeningHourSerializer, PlaceSerializer, ImageSerializer, RateSerializer, ReviewSerializer, ResturantSerializer, MedicalClinicSerializer, MedicalClinicSerializer, GroceryStoreSerializer
from .models import Place, MedicalClinic, GroceryStore, CarRepair, Resturant, Review, Rate, City, Governorate, Address, Phone, Social, OpeningHour, Image, Review
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.

class PlaceModelViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class RestaurantModelViewSet(ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()


class MedicalClinicModelViewSet(ModelViewSet):
    queryset = MedicalClinic.objects.all()
    serializer_class = MedicalClinicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class GroceryStoreModelViewSet(ModelViewSet):
    queryset = GroceryStore.objects.all()
    serializer_class = GroceryStoreSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()
