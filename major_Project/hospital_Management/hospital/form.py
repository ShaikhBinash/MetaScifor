from django import forms
from .models import Hospital

class UpdateHospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ('user',)


