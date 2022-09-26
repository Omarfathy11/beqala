from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.decorators import action

from .serializers import GovernorateSerializer, CitySerializer, AddressSerializer
from .serializers import PhoneSerializer, SocialSerializer, OpeningHourSerializer
from .serializers import PlaceSerializer, ResturantSerializer, MedicalClinicSerializer
from .serializers import GovernorateSerializer, GroceryStoreSerializer, CarRepairSerializer, ImageCollectionSerializer

from .models import Place, MedicalClinic, GroceryStore, CarRepair, Resturant, Review, Rate, City, Governorate, ImageCollection
from .models import Address, Phone, Social, OpeningHour, Review

from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, ViewSetMixin, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

import django_filters.rest_framework
import django_filters
from user.authentication import TokenAuthentication
from rest_framework import pagination
from rest_framework import status
from rest_framework.parsers import MultiPartParser, JSONParser, FileUploadParser, FormParser

class ImageCollectionModelViewSet(ModelViewSet, ViewSetMixin):
    queryset = ImageCollection.objects.all()
    serializer_class = ImageCollectionSerializer
    authentication_classes = []
    parser_classes = (MultiPartParser, JSONParser, FileUploadParser, FormParser)
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'partial_update', 'update']:
            self.permission_classes =[]
            #self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class RestaurantModelViewSet(ModelViewSet):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    parser_classes = (MultiPartParser, JSONParser, FileUploadParser, FormParser)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = Resturant()
    filterset_fields = ['Place_Name']
    #pagination_class = LargeResultsSetPagination


    def get_permissions(self):
        if self.action in ['create', 'destroy', 'partial_update', 'update']:
            self.permission_classes =[]
            #self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class MedicalClinicModelViewSet(ModelViewSet):
    queryset = MedicalClinic.objects.all()
    serializer_class = MedicalClinicSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = MedicalClinic()
    filterset_fields = ['Place_Name']
    #pagination_class = LargeResultsSetPagination

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'partial_update', 'update']:
            self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class GroceryStoreModelViewSet(ModelViewSet):
    queryset = GroceryStore.objects.all()
    serializer_class = GroceryStoreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['Place_Name']
    #pagination_class = LargeResultsSetPagination

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'partial_update', 'update']:
            self.permission_classes =[]
        return super().get_permissions()

class CarRepairModelViewSet(ModelViewSet):
    queryset = CarRepair.objects.all()
    serializer_class = CarRepairSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['Place_Name']

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'partial_update', 'update']:
            self.permission_classes =[]
        return super().get_permissions()


# class PlaceModelViewSet(ModelViewSet):
    #  queryset = Place.objects.all()
    #  serializer_class = PlaceSerializer
    #  authentication_classes = [TokenAuthentication]
    #  permission_classes = [IsAuthenticatedOrReadOnly]
    #  filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #  filterset_fields = ['Place_Name']


    #  def get_permissions(self):
    #      if self.request.method =='post' or self.request.method == 'patch' or self.request.method =='delete':
    #          self.permission_classes =[IsAuthenticated]
    #      return super().get_permissions()
