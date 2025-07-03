from django.urls import path
from enroll import views

urlpatterns = [
    path('enroll/', views.enroll_now, name='enroll_now'),
]