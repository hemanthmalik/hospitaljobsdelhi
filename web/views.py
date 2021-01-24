from django.shortcuts import render, render
from django.http import HttpResponse
from . import forms

# Create your views here.
def home(request):
    return render(request, 'web/home.html', {'myform': forms.ContactForm()})

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
        print(request.POST)
    return render(request, 'web/register.html')

def recruit(request):
    if request.method=="POST":
        print(request.POST)
    return render(request, 'web/recruit.html', {'job_form': forms.JobSeekerForm})