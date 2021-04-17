from django.shortcuts import render, redirect
from django.http import HttpResponse
import mimetypes
from . import forms
from . import models
from . import tasks
from django.views.generic import ListView

# Create your views here.
class HomeView(ListView):
    model = models.JobSeeker
    context_object_name = 'registrations'
    template_name = 'web/home.html'

    def head(self, *args, **kwargs):
        last_applications = self.get_queryset().latest('applied_at')
        response = HttpResponse(
            # RFC 1123 date format.
            headers={'Last-Modified': last_application.applied_at.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response

def register(request):
    if request.method=="POST":
        f = forms.JobSeekerForm(request.POST, request.FILES)
        if f.is_valid():
            data = f.save()
            tasks.send_custom_mail(data)
            return render(request, 'web/submission_success.html', {'ref_id': f"HSD-JS-{data.id}"})
    return render(request, 'web/register.html', {'job_form': forms.JobSeekerForm(), 'current_page':'register'})

def recruit(request):
    if request.method=="POST":
        f = forms.JobPostingForm(request.POST, request.FILES)
        if f.is_valid():
            data = f.save()
            return render(request, 'web/submission_success.html', {'ref_id': f"HSD-JP-{data.id}"})
    return render(request, 'web/recruit.html', {'posting_form': forms.JobPostingForm()})

def get_resume(request, jid=0):
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

