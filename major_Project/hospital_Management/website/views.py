from django.shortcuts import render, get_object_or_404
from hospital.models import Hospital
from doctor.models import BookAppoinment, Doctor
from .filters import DoctorFilter  # Correct import for filtering

def home(request):
    filter = DoctorFilter(request.GET, queryset=Doctor.objects.select_related('hospital').all())  # Query Doctors
    context = {'filter': filter}
    return render(request, 'website/home.html', context)
    
def about_us(request):
    return render(request, 'website/about_us.html')

def doctor_listing(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}  # Wrap in a dictionary
    return render(request, 'website/doctor_listing.html', context)


def doctor_details(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)  # ✅ Fetch the correct doctor
    has_applied = False

    if request.user.is_authenticated:  
        has_applied = BookAppoinment.objects.filter(user=request.user, doctor=doctor).exists()

    context = {'doctor': doctor, 'has_applied': has_applied}
    return render(request, 'website/doctor_details.html', context)
