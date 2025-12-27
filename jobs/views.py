from django.shortcuts import render, redirect
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def post_job(request):
    if request.method == 'POST':
        Job.objects.create(
            employer=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            skills=request.POST['skills'],
            location=request.POST['location']
        )
        return redirect('employer_dashboard')
    return render(request, 'jobs/post_job.html')
