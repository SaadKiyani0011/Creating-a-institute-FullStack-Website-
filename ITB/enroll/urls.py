from django.urls import path
from enroll import views
urlpatterns = [
    path('apply/',views.enroll,name='apply')
]
