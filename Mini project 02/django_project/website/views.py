from django.shortcuts import render, get_object_or_404
from job.models import Job, ApplyJob
from .filter import Jobfilter

def home(request):
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    context = {'filter':filter}
    return render(request, 'website/home.html',context)


def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs':jobs}
    return render(request, 'website/job_listing.html', context)


def job_details(request, pk):
    job = get_object_or_404(Job, pk=pk)
    has_applied = False

    if request.user.is_authenticated:  # Check if the user is logged in
        has_applied = ApplyJob.objects.filter(user=request.user, job=job).exists()

    context = {'job': job, 'has_applied': has_applied}
    return render(request, 'website/job_details.html', context)
