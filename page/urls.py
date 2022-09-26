from django.urls import path, include
from page import views
from rest_framework.routers import DefaultRouter


route = DefaultRouter()
#route.register(r'places', views.PlaceModelViewSet)
route.register(r'images', views.ImageCollectionModelViewSet)
route.register(r'restaurants', views.RestaurantModelViewSet)
route.register(r'groceries', views.GroceryStoreModelViewSet)
route.register(r'medical-clinics', views.MedicalClinicModelViewSet)
route.register(r'carrepair', views.CarRepairModelViewSet)

urlpatterns = [
    path('', include(route.urls)),
    
]

