from django.urls import path
from about import views
urlpatterns = [
    path('aboutus/',views.about,name='aboutus')
]
