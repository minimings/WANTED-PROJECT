from django.db import models

class FileResume(models.Model):
    title        = models.CharField(max_length = 45)
    file_resume  = models.FileField(max_length = 2000)
    general_user = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'file_resumes'