from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from .form import UpdateCompanyForm
from users.models import User
from django.views.decorators.csrf import csrf_exempt

#update company
@csrf_exempt
def update_company(request):
    if request.user.is_recruiter:
        try:
            company = Company.objects.get(user=request.user)  # Ensure company exists
        except Company.DoesNotExist:
            messages.error(request, "Company not found!")
            return redirect('dashboard')  # Redirect if no company found

        if request.method == 'POST':  # Fixed 'POSt' typo
            form = UpdateCompanyForm(request.POST, instance=company)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True  # Ensure `has_company` field exists in `User` model
                var.save()
                user.save()
                messages.success(request, 'Your company info has been updated!')
                return redirect('dashboard')  # Ensure 'dashboard' is a valid URL name
            else:
                messages.warning(request, 'Something went wrong')

        else:
            form = UpdateCompanyForm(instance=company)

        context = {'form': form}  # Ensure context is always passed
        return render(request, 'company/update_company.html', context)
    else:
        messages.warning(request, 'Permission denied')
        return redirect('dashboard')


#view company details
def comapny_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company':company}
    return render(request, 'company/company_details.html', context)




