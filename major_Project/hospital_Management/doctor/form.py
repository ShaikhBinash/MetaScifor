from django import forms
from .models import Doctor

class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialities', 'timing', 'appointment_fees', 'qr_code','email']


class UpdateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ('user', 'doctor')
