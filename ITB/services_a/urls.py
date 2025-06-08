from django.urls import path 
from services_a import views
urlpatterns = [
    path('service/',views.services,name='services')
]