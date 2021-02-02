from django.shortcuts import render, redirect
from django.http import HttpResponse
import mimetypes
from . import forms
from . import models
from . import tasks

# Create your views here.
def home(request):
    registrations = models.JobSeeker.objects.all()[:10]
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
            return render(request, 'web/submission_success.html', {'ref_id': f"HSD-JS-{5000+data.id}"})
    return render(request, 'web/register.html', {'job_form': forms.JobSeekerForm(), 'current_page':'register'})

def recruit(request):
    if request.method=="POST":
        f = forms.JobPostingForm(request.POST, request.FILES)
        if f.is_valid():
            data = f.save()
            return render(request, 'web/submission_success.html', {'ref_id': f"HSD-JP-{5000+data.id}"})
    return render(request, 'web/recruit.html', {'posting_form': forms.JobPostingForm()})

def get_resume(request, jid=0):
    print(request.user.is_superuser)
    if request.user.is_superuser:
        try:
            current_jobseeker = models.JobSeeker.objects.get(id=jid)
            if current_jobseeker.resume:   
                filename = current_jobseeker.resume.name
                response = HttpResponse(current_jobseeker.resume, content_type=mimetypes.guess_type(filename)[0])
                response['Content-Length'] = current_jobseeker.resume.size
                response['Content-Disposition'] = "attachment; filename=" + filename
                return response
        except:
            pass
    return redirect('/')
