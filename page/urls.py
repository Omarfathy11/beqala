from django.urls import path, include
from page import views
from rest_framework.routers import DefaultRouter


route = DefaultRouter()
# route.register(r'places', views.PlaceModelViewSet)
route.register(r'restaurants', views.RestaurantModelViewSet)
# route.register(r'groceries', views.RestaurantModelViewSet)
# route.register(r'medical-clinics', views.RestaurantModelViewSet)
#route.register(r'carrepair', views.)

print('Hello')
urlpatterns = [
    path('', include(route.urls)),
    #path('restaurants/', views.RestaurantModelViewSet),
    #path('groceries/', views.GroceryStoreModelViewSet),
    #path('medical-clinics/', views.MedicalClinicModelViewSet),
    #path('resturants/<int:pk>', ),
    #path('groceries/<int:pk>', ),
    #path('medical-clinics/<int:pk>', ),
]
