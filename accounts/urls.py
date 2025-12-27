from django.urls import path
from . import views

app_name = 'accounts'   

urlpatterns = [
    path('employer/register/', views.employer_register, name='employer_register'),
    path('jobseeker/register/', views.jobseeker_register, name='jobseeker_register'),

    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('jobseeker/dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
]