from django.db import models

class Job(models.Model):
    name      = models.CharField(max_length = 45)
    job_group = models.ForeignKey('postings.JobGroup', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'jobs'

    def __str__(self):
        return self.name