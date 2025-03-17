from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient
from users.models import User
from .form import UpdatePatientForm


def update_patient(request):
    if request.user.is_patient:
        patient, created = Patient.objects.get_or_create(user=request.user)  # Ensures Patient object exists

        if request.method == 'POST':
            form = UpdatePatientForm(request.POST, instance=patient)
            if form.is_valid():
                var = form.save(commit=False)
                user = request.user
                user.has_profile = True  
                var.save()
                user.save()
                messages.success(request, 'Your profile has been updated.')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong.')
        else:
            form = UpdatePatientForm(instance=patient)

        context = {'form': form}
        return render(request, 'patient/update_patient.html', context)

    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')



def patient_details(request, pk):
    patient = Patient.objects.get(pk=pk)
    context = {'patient':patient}
    return render(request, 'patient/patient_details.html',context)
 

