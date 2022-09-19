from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import viewsets_user
from rest_framework.authtoken import views

route = DefaultRouter()
route.register(r'user', viewsets_user)

urlpatterns = [
path('', include(route.urls)),   
path('token/',views.obtain_auth_token),
#path('', viewsets_user),
]
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]