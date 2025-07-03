from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_list, name='courses'),
    path('category/<slug:category_slug>/', views.course_list, name='course_list_by_category'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
]
