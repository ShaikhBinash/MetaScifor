from django.urls import path
from . import views

urlpatterns = [
    path('register-patient/', views.register_patient, name= 'register-patient'),
    path('register-admin/', views.register_admin, name= 'register-admin'),
    path('login/', views.login_user, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
]