from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class JobCreate(CreateView):
    model = Jobs
    fields = ('company', 'job_title', 'date', 'description')

class JobUpdate(UpdateView):
    model = Jobs
    fields =  ('company', 'job_title', 'date', 'description')

class JobDelete(DeleteView):
    model = Jobs
    success_url = '/jobs/'