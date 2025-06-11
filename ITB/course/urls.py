from django.urls import path
from course import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
]