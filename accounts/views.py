from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployerSignupForm, JobSeekerSignupForm

def employer_register(request):
    form = EmployerSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('accounts:employer_dashboard')
    return render(request, 'accounts/register.html', {'form': form})


def jobseeker_register(request):
    form = JobSeekerSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('accounts:jobseeker_dashboard')
    return render(request, 'accounts/register.html', {'form': form})


def employer_dashboard(request):
    return render(request, 'dashboards/employer_dashboard.html')


def jobseeker_dashboard(request):
    return render(request, 'dashboards/jobseeker_dashboard.html')