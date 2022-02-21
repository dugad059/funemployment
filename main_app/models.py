from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Jobs(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date = models.DateField('Application Submitted')
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('detail_jobs', kwargs={'job_id': self.id})


class Response(models.Model):
    date = models.DateField('Response Date')
    responce_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    notes = models.TextField(max_length=250)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.responce_name

class Reach(models.Model):
    date = models.DateField('Reachout Date')
    reach_name = models.CharField('Reachout Date', max_length=100)
    source = models.CharField(max_length=100)
    notes = models.TextField(max_length=250)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.reach_name

