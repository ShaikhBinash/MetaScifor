from django import forms
from .models import Patient

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('user',)