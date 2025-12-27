from django.shortcuts import redirect
from .models import Application
from jobs.models import Job

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        Application.objects.create(
            job=job,
            applicant=request.user,
            resume=request.FILES['resume']
        )
        return redirect('accounts:jobseeker_dashboard') 