from django.urls import path
from course import views

urlpatterns = [
    path('courses/',views.course,name='courses')
]
