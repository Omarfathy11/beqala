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
from .serializers import GovernorateSerializer, GroceryStoreSerializer, CarRepairSerializer, ImageCollectionSerializer#, ListResturantSerializer

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

from rest_framework import parsers
from formencode.variabledecode import variable_decode


class MultipartFormencodeParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        data = variable_decode(result.data)
        return parsers.DataAndFiles(data, result.files)

class ImageCollectionModelViewSet(ModelViewSet, generics.CreateAPIView):
    queryset = ImageCollection.objects.all()
    serializer_class = ImageCollectionSerializer
    authentication_classes = []
    parser_classes = (MultiPartParser, JSONParser, FileUploadParser, FormParser)
    permission_classes = []
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


    @action(methods=['post'], detail=True, permission_classes=[])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        image = ImageCollection.objects.create(image=file)

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'partial_update', 'update']:
            self.permission_classes =[]
            #self.permission_classes =[IsAuthenticated]
        return super().get_permissions()

class RestaurantModelViewSet(ModelViewSet, generics.CreateAPIView, generics.ListAPIView):
    queryset = Resturant.objects.all()
    serializer_class = ResturantSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    parser_classes = (MultiPartParser, JSONParser, FileUploadParser, FormParser)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    #filterset_class = Resturant()
    filterset_fields = ['Place_Name']
    #pagination_class = LargeResultsSetPagination

    # def get_queryset(self):
    #     return ImageCollection.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         self.serializer_class = ListResturantSerializer
    #     return super().get_serializer_class()

    @action(methods=['post'], detail=True, permission_classes=[])
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        image = ImageCollection.objects.create(image=file)
        return Response(serializer.data.file)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}


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
