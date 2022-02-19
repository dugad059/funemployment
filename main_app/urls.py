from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.index_jobs, name='index_jobs'),
    path('jobs/<int:job_id>/', views.detail_jobs, name='detail_jobs'),
    path('jobs/create/', views.JobCreate.as_view(), name='create_jobs'),
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='update_jobs'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='delete_jobs'),

]