from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.index_jobs, name='index_jobs'),
    path('jobs/<int:job_id>/', views.detail_jobs, name='detail_jobs'),

]