from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hospital
from .form import UpdateHospitalForm
from users.models import User
from django.views.decorators.csrf import csrf_exempt

# Update hospital details
@csrf_exempt
def update_hospital(request):
    if request.user.is_admin:
        hospital, created = Hospital.objects.get_or_create(user=request.user)  # Get or create hospital
        
        if request.method == 'POST':
            form = UpdateHospitalForm(request.POST, instance=hospital)
            if form.is_valid():
                var = form.save(commit=False)
                user = request.user
                user.has_hospital = True  # Ensure the `has_hospital` field exists in `User` model
                var.save()
                user.save()
                messages.success(request, 'Your hospital info has been updated!')
                return redirect('dashboard')  
            else:
                messages.warning(request, 'Something went wrong')

        else:
            form = UpdateHospitalForm(instance=hospital)

        return render(request, 'hospital/update_hospital.html', {'form': form})
    
    else:
        messages.warning(request, 'Permission denied')
        return redirect('dashboard')


# View hospital details
def hospital_details(request, pk):
    hospital = Hospital.objects.get(pk=pk)
    context = {'hospital': hospital}
    return render(request, 'hospital/hospital_details.html', context)
