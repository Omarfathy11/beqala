from django.urls import path, include
from page import views


urlpatterns = [
    path('places/', views.PlaceModelViewSet.as_view({'get': 'list'})),
    path('resturants/', views.RestaurantModelViewSet.as_view({'get': 'list'})),
    path('groceries/', views.GroceryStoreModelViewSet.as_view({'get': 'list'})),
    path('medical-clinics/', views.MedicalClinicModelViewSet.as_view({'get': 'list'})),
    #path('resturants/<int:pk>', ),
    #path('groceries/<int:pk>', ),
    #path('medical-clinics/<int:pk>', ),
]
