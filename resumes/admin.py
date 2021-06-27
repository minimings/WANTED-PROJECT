from django.contrib import admin

from resumes.models import FileResume

class FileResumeAdmin(admin.ModelAdmin):
    list_display       = ['general_user', 'title', 'file_resume']
    list_display_links = ['general_user']

admin.site.register(FileResume, FileResumeAdmin)