from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Jobs
from .forms import ReoutForm, RespForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
"""
=============================
      MAIN ROUTES
=============================

"""
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_jobs')
        else:
            error_message = 'Invalid Sign Up - Please Try Again'
    form = UserCreationForm()
    context = {'form' : form, 'error_message' : error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

"""
=============================
      JOBS ROUTES
=============================

"""

@login_required
def index_jobs(request):
    jobs = Jobs.objects.filter(user=request.user)
    return render(request, 'jobs/index.html', { 'jobs' : jobs })

@login_required
def detail_jobs(request, job_id):
    job = Jobs.objects.get(id=job_id)
    reout_form = ReoutForm()
    resp_form = RespForm()
    return render(
        request, 
        'jobs/detail.html', 
        { 'job' : job,
         'reout_form' : reout_form,
        'resp_form' : resp_form,
        })

def add_reachout(request, job_id):
    form = ReoutForm(request.POST)
    if form.is_valid():
        new_reach = form.save(commit=False)
        new_reach.job_id = job_id
        new_reach.save()
    return redirect('detail_jobs', job_id=job_id)

def add_response(request, job_id):
    form = RespForm(request.POST)
    if form.is_valid():
        new_reach = form.save(commit=False)
        new_reach.job_id = job_id
        new_reach.save()
    return redirect('detail_jobs', job_id=job_id)

class JobCreate(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ('company', 'job_title', 'date', 'description')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields =  ('company', 'job_title', 'date', 'description')

class JobDelete(LoginRequiredMixin, DeleteView):
    model = Jobs
    success_url = '/jobs/'

