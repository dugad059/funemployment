from datetime import date
from django.db import models

# Create your models here.

class Jobs(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    date = models.DateField('Application Submitted')
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.company