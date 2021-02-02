from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields] + ['file_link']

@admin.register(models.JobPosting)
class JobSeekerAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]