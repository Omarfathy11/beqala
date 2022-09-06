from django.urls import path, include
from page import views


urlpatterns = [
    path('places/', views.PlaceModelViewSet),
    path('resturants/', views.RestaurantModelViewSet),
    path('groceries/', views.GroceryStoreModelViewSet),
    path('medical-clinics/', views.MedicalClinicModelViewSet),
    path('resturants/<int:pk>', views.RestaurantModelViewSet),
    path('groceries/<int:pk>', views.GroceryStoreModelViewSet),
    path('medical-clinics/<int:pk>', views.MedicalClinicModelViewSet),
]
