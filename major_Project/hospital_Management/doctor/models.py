from django.db import models
from users.models import User
from hospital.models import Hospital



class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Track which user created the doctor
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=1)
    
    SPECIALITIES = [
        ('General Physician', 'General Physician'),
        ('Pediatrician', 'Pediatrician'),
        ('Cardiologist', 'Cardiologist'),
        ('Neurologist', 'Neurologist'),
        ('Orthopedic Surgeon', 'Orthopedic Surgeon'),
        ('Gynecologist/Obstetrician', 'Gynecologist/Obstetrician'),
        ('Dermatologist', 'Dermatologist'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Psychiatrist', 'Psychiatrist'),
        ('General Surgeon', 'General Surgeon'),
    ]

    name = models.CharField(max_length=255)
    specialities = models.CharField(max_length=30, choices=SPECIALITIES)
    timing = models.CharField(max_length=20, choices=[
        ('08:00-12:00', '08:00 AM - 12:00 PM'),
        ('12:00-16:00', '12:00 PM - 04:00 PM'),
        ('16:00-20:00', '04:00 PM - 08:00 PM'),
        ('24/7', 'Available 24/7'),
    ])
    appointment_fees = models.DecimalField(max_digits=10, decimal_places=2)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    def __str__(self):
        return self.name


class BookAppoinment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Patient/User
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")  # ✅ Add related_name
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')])





    
