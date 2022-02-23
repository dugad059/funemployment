from tkinter import Widget
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



class Jobs(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date = models.DateField('Date (YYYY/MM/DD)')
    description = models.TextField('Notes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('detail_jobs', kwargs={'job_id': self.id})

