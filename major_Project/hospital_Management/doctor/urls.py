from django.urls import path
from . import views

urlpatterns = [
    path('create-doctor/', views.create_doctor, name= 'create-doctor'),
    path('update-doctor/<int:pk>', views.update_doctor, name= 'update-doctor'),
    path('manage-appoinment/', views.manage_appointments,name='manage-appoinment'),
    path('booked-appointments', views.booked_appointments, name='booked-appointments'),
    path('doctor/book-appointment/<int:pk>/', views.book_appointment, name='book-appointment'),
    path('doctor/all-patients/<int:pk>/', views.all_patients, name='all-patients'),
    path('send-confirmation-email/<int:patient_id>/', views.send_confirmation_email, name='send_confirmation_email'),
    path('send-doctor-patient-list/<int:doctor_id>/', views.send_doctor_patient_list, name='send_doctor_patient_list'),
    path('payment-success/', views.payment_success, name='payment-success')
]


