from django.shortcuts import render
from .models import Jobs


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index_jobs(request):
    jobs = Jobs.objects.all()
    return render(request, 'jobs/index.html', { 'jobs' : jobs })

def detail_jobs(request, job_id):
    job = Jobs.objects.get(id=job_id)
    return render(request, 'jobs/detail.html', { 'job' : job })