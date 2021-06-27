from django.contrib import admin

from tinymce         import HTMLField
from tinymce.widgets import TinyMCE

from postings.models import Company, JobPosting, JobPostingImage, Icon

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_mainview', 'nation', 'job_group']

    formfield_overrides = {
        HTMLField: {'widget' : TinyMCE()}
    }

class JobPostingAdmin(admin.ModelAdmin):
    list_display       = ['title', 'description', 'deadline', 'company']
    list_display_links = ['title', 'company']

    formfield_overrides = {
        HTMLField: {'widget' : TinyMCE()}
    }

class JobPostingImageAdmin(admin.ModelAdmin):
    list_display       = ['job_posting_image', 'job_posting']
    list_display_links = ['job_posting_image', 'job_posting']

class IconAdmin(admin.ModelAdmin):
    list_display       = ['icon', 'company']
    list_display_links = ['icon', 'company']

admin.site.register(Icon, IconAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(JobPostingImage, JobPostingImageAdmin)