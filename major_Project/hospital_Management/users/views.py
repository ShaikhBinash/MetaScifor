from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
 
# from company.models import Company


# Register Patient
def register_patient(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            try:
                var = form.save(commit=False)
                var.is_patient = True
                var.username = var.email  # Ensure username is email
                var.save()

                messages.success(request, 'Your account has been created. Please login.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Error: {e}")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")  # Properly format errors

    else:
        form = RegisterUserForm()

    return render(request, 'users/register_patient.html', {'form': form})

# Register Admin
def register_admin(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            try:
                var = form.save(commit=False)
                var.is_admin = True
                var.username = var.email  # Ensure username is email
                var.save()

                messages.success(request, 'Your account has been created. Please login.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Error: {e}")
                print(f"Database Error: {e}")  # Debugging info
        else:
            print(form.errors)  # Debugging info
            messages.error(request, f"Form Errors: {form.errors}")  # Show form errors

    else:
        form = RegisterUserForm()

    return render(request, 'users/register_admin.html', {'form': form})


            
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Uses email

        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid email or password')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')


       
def logout_user(request):
    logout(request)
    messages.info(request, 'Your Session has ended')
    return redirect('login')


