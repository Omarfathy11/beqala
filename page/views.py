from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from .serializers import GovernorateSerializer, CitySerializer, AddressSerializer, PhoneSerializer, SocialSerializer, OpeningHourSerializer, PlaceSerializer, RateSerializer, ReviewSerializer, ResturantSerializer, MedicalClinicSerializer, MedicalClinicSerializer, GroceryStoreSerializer
from .models import Place, MedicalClinic, GroceryStore, CarRepair, Resturant, Review, Rate, City, Governorate, Address, Phone, Social, OpeningHour, Review
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
import django_filters.rest_framework
import django_filters
from collections import namedtuple
from rest_framework.parsers import JSONParser




# Create your views here.

class PlaceModelViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['Place_Name']
    parser_classes = [JSONParser]


    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class RestaurantModelViewSet(ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = Resturant()
    filterset_fields = ['Place_Name']
    parser_classes = [JSONParser]

    #pagination_class = LargeResultsSetPagination

    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()


class MedicalClinicModelViewSet(ModelViewSet):
    queryset = MedicalClinic.objects.all()
    serializer_class = MedicalClinicSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = MedicalClinic()
    filterset_fields = ['name']
    #pagination_class = LargeResultsSetPagination

    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class GroceryStoreModelViewSet(ModelViewSet):
    queryset = GroceryStore.objects.all()
    serializer_class = GroceryStoreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']
    #pagination_class = LargeResultsSetPagination

    def get_permissions(self):
        if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

'''
class CarRepairModelViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['Place_Name']
'''