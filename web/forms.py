from django import forms
from django.forms import ModelForm
from django.db import models
from .models import JobSeeker

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class JobSeekerForm(ModelForm):
    field_names = {'first_name': 'test'}

    # def add_prefix(self, field_name):
    #     field_name = self.field_names.get(field_name, field_name)
    #     return super(JobSeekerForm, self).add_prefix(field_name)

    class Meta:
        model = JobSeeker
        fields = ('first_name', 'last_name')
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

    def __init__(self, *args, **kwargs):
        super(JobSeekerForm, self).__init__(*args, **kwargs)
        print(self.fields['first_name'].widget.attrs)
        self.fields['first_name'].widget.attrs={'placeholder': 'Enter first name', 'class': 'form-control', 'name': 'test'}
        self.fields['last_name'].widget.attrs={'placeholder': 'Enter last name', 'class': 'form-control'}
        # for visible in self.visible_fields():
        #     elem = visible.field.widget
        #     elem.attrs['class'] = 'form-control'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

GEEKS_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    sollicitanten = forms.ChoiceField(choices = GEEKS_CHOICES)
    vacature_contract = forms.ChoiceField(choices = GEEKS_CHOICES)