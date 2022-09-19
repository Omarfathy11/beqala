import imp
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from .authentication import TokenAuthentication
from django.core.paginator import Paginator

class viewsets_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAdminUser]

    

