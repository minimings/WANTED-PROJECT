from django.db import models

class WriteResume(models.Model):
    title           = models.CharField(max_length = 45)
    name            = models.CharField(max_length = 45)
    email           = models.EmailField(max_length = 45)
    phone_number    = models.CharField(max_length = 45)
    description     = models.TextField()
    general_user    = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    complete_status = models.ForeignKey('resumes.CompleteStatus', on_delete = models.SET_NULL, null = True)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'write_resumes'