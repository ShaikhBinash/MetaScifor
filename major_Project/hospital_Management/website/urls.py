from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about_us, name='about'),
    path('doctor-listing/', views.doctor_listing, name= 'doctor-listing'),
    path('doctor-details/<int:pk>/', views.doctor_details, name='doctor-details')
]


