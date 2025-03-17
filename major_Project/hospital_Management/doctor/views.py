#razorpay import
import razorpay
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Doctor, BookAppoinment
from .form import CreateDoctorForm, UpdateDoctorForm
from django.db.models import Count
from django.core.mail import send_mail
from django.conf import settings
from patient.models import Patient
from django.http import JsonResponse


# Initialize Razorpay client with Test API keys
razorpay_client = razorpay.Client(auth=("rzp_test_GLzmpRkZhIzpAE", "YMYCq9kBMmdsjlNHefY4n6II"))

# Create doctor (replacing create_job)
def create_doctor(request):
    if getattr(request.user, 'is_admin', False) and getattr(request.user, 'has_hospital', False):
        if request.method == 'POST':
            form = CreateDoctorForm(request.POST, request.FILES)  # Include request.FILES for image uploads
            if form.is_valid():
                doctor = form.save(commit=False)
                doctor.hospital = request.user.hospital  # Assign hospital correctly
                doctor.save()
                messages.success(request, 'New doctor has been added successfully!')
                return redirect('dashboard')
            else:
                print("\nForm Errors:", form.errors)  # Print errors in terminal
                messages.warning(request, 'Something went wrong. Please check the form fields.')
        else:
            form = CreateDoctorForm()

        context = {'form': form}
        return render(request, 'doctor/create_doctor.html', context)
    
    messages.warning(request, 'Permission Denied')
    return redirect('dashboard')




# Update department (replacing update_job)
def update_doctor(request, pk):
    department = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateDoctorForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.info(request, 'Department info updated successfully.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong.')
    else:
        form = UpdateDoctorForm(instance=department)
        context = {'form': form}
        return render(request, 'doctor/update_doctor.html', context)


# Manage appointments (replacing manage_jobs)
def manage_appointments(request):
    doctors = Doctor.objects.filter(hospital=request.user.hospital).annotate(
    num_patients=Count('appointments')  # ✅ Use related_name
)
    
    context = {'doctors': doctors}
    return render(request, 'doctor/manage_appointment.html', context)



# Book appointment (replacing apply_to_job)
def book_appointment(request, pk):
    """Handles appointment booking and initiates Razorpay payment."""
    if not request.user.is_authenticated:
        messages.info(request, 'Please log in to continue')
        return redirect('login')

    doctor = get_object_or_404(Doctor, pk=pk)

    if BookAppoinment.objects.filter(user=request.user, doctor=doctor).exists():
        messages.warning(request, 'You have already booked an appointment with this doctor.')
        return redirect('dashboard')

    # Save appointment as "Pending" before payment
    appointment = BookAppoinment.objects.create(
        doctor=doctor,
        user=request.user,
        status="Pending"
    )

    # 🔹 Convert Decimal to int before passing to Razorpay
    order_amount = int(doctor.appointment_fees * 100)  # Convert ₹ to paise (integer)

    # Razorpay Order creation
    order_data = {
        "amount": order_amount,
        "currency": "INR",
        "receipt": f"appointment_{pk}_{request.user.id}",
        "payment_capture": 1  # Auto-capture payment
    }

    order = razorpay_client.order.create(data=order_data)

    # Pass order details to the template
    context = {
        "doctor": doctor,
        "order_id": order["id"],
        "amount": order_amount / 100,  # Convert paise back to rupees for display
        "key": "rzp_test_GLzmpRkZhIzpAE",
        "appointment_id": appointment.pk
    }

    return render(request, 'website/payment.html', context)

    
#payment success
# views.py

def payment_success(request):
    """Handles successful payment and updates the appointment status."""
    if request.method == "POST":
        payment_id = request.POST.get("razorpay_payment_id")
        order_id = request.POST.get("razorpay_order_id")
        
        # Extract doctor ID from the order receipt
        appointment_id = request.POST.get("appointment_id")
        appointment = get_object_or_404(BookAppoinment, id=appointment_id)

        # Mark the appointment as confirmed and update the patient payment status
        appointment.status = "Confirmed"
        appointment.payment_id = payment_id
        appointment.save()

        # Ensure the user has a related patient, or create one
        user = appointment.user
        patient, created = Patient.objects.get_or_create(user=user)

        # Update the is_paid status
        patient.is_paid = True
        patient.save()

        messages.success(request, "Appointment booked and payment confirmed successfully!")
        return redirect("dashboard")

    messages.error(request, "Payment failed. Please try again.")
    return redirect("home")



# View all patients (replacing all_applicants)
def all_patients(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    appointments = doctor.appointments.select_related("user").all()

    # Get patients related to those appointments
    patients = Patient.objects.filter(user__in=[app.user for app in appointments])

    context = {
        'doctor': doctor,
        'patients': patients
    }
    return render(request, 'doctor/all_patients.html', context)

#send confirmation mail to paitent
def send_confirmation_email(request, patient_id):
    patient = get_object_or_404(BookAppoinment, id=patient_id)
    user_email = patient.user.email
    
    subject = "Appointment Confirmation"
    message = f"Dear {patient.user.first_name},\n\nYour appointment with Dr. {patient.doctor.name} has been confirmed!\n\nThank you!"
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  
        [user_email],
        fail_silently=False,
    )
    messages.success(request, f"Confirmation email sent to {user_email}")
    return redirect('all-patients', pk=patient.doctor.pk)

#send patient list to doctor

def send_doctor_patient_list(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    # Fetch patients based on appointments linked to this doctor
    patients = Patient.objects.filter(user__in=doctor.appointments.values_list('user', flat=True))

    if not patients.exists():
        messages.warning(request, "No patients found for this doctor.")
        return redirect('all-patients', pk=doctor.id)

    # Construct patient list
    patient_list = "\n".join([f"{p.first_name} {p.surname} ({p.email})" for p in patients])

    subject = f"Patient List for Dr. {doctor.name}"
    message = f"Dear Dr. {doctor.name},\n\nHere is the list of patients who have booked appointments:\n\n{patient_list}\n\nBest regards,\nHospital Management System"

    # Ensure the doctor has an email before sending
    if not doctor.email:
        messages.error(request, "Doctor does not have an email address.")
        return redirect('all-patients', pk=doctor.id)

    # Send email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [doctor.email],
        fail_silently=False,
    )

    messages.success(request, f"Patient list sent to Dr. {doctor.name} ({doctor.email})")
    return redirect('all-patients', pk=doctor.id)



# View booked appointments (replacing applied_jobs)
def booked_appointments(request):
    appointments = BookAppoinment.objects.filter(user=request.user)
    context = {'appointments': appointments}  # Keep the correct naming
    return render(request, 'doctor/booked_appointments.html', context)
