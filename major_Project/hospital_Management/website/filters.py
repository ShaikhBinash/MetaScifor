import django_filters
from doctor.models import Doctor
from hospital.models import Hospital

class DoctorFilter(django_filters.FilterSet):

    SPECIALITY_CHOICES = [
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

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label="Doctor Name")
    specialities = django_filters.ChoiceFilter(choices=SPECIALITY_CHOICES, field_name='specialities', label="Speciality")
    hospital = django_filters.ModelChoiceFilter(queryset=Hospital.objects.all(), field_name='hospital', label="Hospital")

    class Meta:
        model = Doctor
        fields = ['name', 'specialities', 'hospital']
