from django.db import models
from users.models import User

class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=30)
    
    START_END_TIME_CHOICES = [
        ('08:00-16:00', '08:00 AM - 04:00 PM'),
        ('09:00-17:00', '09:00 AM - 05:00 PM'),
        ('10:00-18:00', '10:00 AM - 06:00 PM'),
        ('24/7', 'Open 24/7'),
    ]
    start_end_time = models.CharField(max_length=20, choices=START_END_TIME_CHOICES)

    def __str__(self):
        return self.name
