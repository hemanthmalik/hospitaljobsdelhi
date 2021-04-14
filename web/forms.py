from django import forms
from django.forms import ModelForm
from django.db import models
from .models import JobSeeker, JobPosting

class JobSeekerForm(ModelForm):
    class Meta:
        model = JobSeeker
        exclude = ('applied_at',)
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

    def __init__(self, *args, **kwargs):
        super(JobSeekerForm, self).__init__(*args, **kwargs)
        self.fields['resume'].widget.attrs={'accept': '.pdf'}
        for visible in self.visible_fields():
            elem = visible.field.widget
            elem.attrs['class'] = 'form-control'
            elem.attrs['placeholder'] = visible.field.label

class JobPostingForm(ModelForm):
    class Meta:
        model = JobPosting
        exclude = ('posted_at',)
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

    def __init__(self, *args, **kwargs):
        super(JobPostingForm, self).__init__(*args, **kwargs)
        self.fields['required_qualification'].widget.attrs={'rows':3}
        for visible in self.visible_fields():
            elem = visible.field.widget
            elem.attrs['class'] = 'form-control'
            elem.attrs['placeholder'] = visible.field.label
