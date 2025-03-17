from django.db import models
from users.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)  # Ensure this field exists
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)  # Ensure email exists
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.surname}'




