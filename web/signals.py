from . import models
from django.db.models.signals import pre_save
from django.db import connection



def initialize_jobseeker(sender, instance, **kwargs):
    if not models.JobSeeker.objects.all().exists():
        cursor = connection.cursor()
        cursor.execute('ALTER SEQUENCE web_jobseeker_id_seq RESTART WITH 51234')

pre_save.connect(initialize_jobseeker, sender=models.JobSeeker)


def initialize_jobposting(sender, instance, **kwargs):
    if not models.JobPosting.objects.all().exists():
        cursor = connection.cursor()
        cursor.execute('ALTER SEQUENCE web_jobposting_id_seq RESTART WITH 21234')

pre_save.connect(initialize_jobposting, sender=models.JobPosting)