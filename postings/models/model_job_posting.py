from django.db import models

from tinymce.models import HTMLField

class JobPosting(models.Model):
    title       = models.CharField(max_length = 45)
    description = HTMLField()
    deadline    = models.DateTimeField()
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    company     = models.ForeignKey('postings.Company', on_delete = models.CASCADE)
    job_group   = models.ForeignKey('postings.JobGroup', on_delete = models.SET_NULL, null = True)
    career      = models.ForeignKey('users.Career', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'job_postings'

    def __str__(self):
        return self.title