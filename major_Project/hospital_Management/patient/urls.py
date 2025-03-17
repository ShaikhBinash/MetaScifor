from django.urls import path
from . import views

urlpatterns = [
    path('update-patient/', views.update_patient, name= 'update-patient'),
    path('patient-details/<int:pk>', views.patient_details, name= 'patient-details'),
]


