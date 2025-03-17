from django.urls import path
from . import views

urlpatterns = [
    path('update-hospital/', views.update_hospital, name='update-hospital'),
    path('hospital-details/<int:pk>', views.hospital_details, name= 'hospital-details'),
]


