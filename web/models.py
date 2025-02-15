from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone
# Create your models here.

GENDER_CHOICES = [
    ('', 'Select Gender'),
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]

class JobSeeker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False)
    phone = models.CharField(max_length=10, default=None)
    email = models.EmailField(max_length=50, default=None)
    qualification = models.CharField(max_length=50, blank=True)
    speciality = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    current_organization = models.CharField(max_length=50, blank=True)
    expected_salary = models.IntegerField(blank=True, null=True)
    resume = models.FileField(upload_to="uploads/", blank=True, null=True)
    applied_at = models.DateTimeField(default=timezone.now)
    
    def file_link(self):
        if self.resume:
            return format_html(f"<a href='{reverse('web:get_resume', kwargs={'jid':self.id})}'>download</a>")
        else:
            return "No attachment"

    file_link.allow_tags = True


class JobPosting(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10)
    contact_email = models.EmailField(max_length=50)
    organization_name = models.CharField(max_length=50)
    required_qualification = models.TextField(max_length=50, blank=True)
    required_experience = models.CharField(max_length=50, blank=True)
    salary_offering = models.CharField(max_length=20, blank=True)
    posted_at = models.DateTimeField(default=timezone.now)
