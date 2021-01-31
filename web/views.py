from django.shortcuts import render, render
from django.http import HttpResponse
from . import forms
from . import models
from . import tasks

# Create your views here.
def home(request):
    registrations = models.JobSeeker.objects.all()
    return render(request, 'web/home.html', {'registrations': registrations})

def about(request):
    return render(request, 'web/about_us.html')

def services(request):
    return render(request, 'web/services.html')

def blog(request):
    return render(request, 'web/blog.html')

def gallery(request):
    return render(request, 'web/gallery.html')

def contact(request):
    return render(request, 'web/contact_us.html')

def register(request):
    if request.method=="POST":
        f = forms.JobSeekerForm(request.POST, request.FILES)
        if f.is_valid():
            data = f.save()
            tasks.send_custom_mail(data)
            return render(request, 'web/submission_success.html')
    return render(request, 'web/register.html', {'job_form': forms.JobSeekerForm(), 'current_page':'register'})

def recruit(request):
    if request.method=="POST":
        f = forms.JobPostingForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return render(request, 'web/submission_success.html')
    return render(request, 'web/recruit.html', {'posting_form': forms.JobPostingForm()})
