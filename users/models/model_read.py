from django.db import models

class Read(models.Model):
    is_read      = models.BooleanField(default = False)
    general_user = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    job_posting  = models.ForeignKey('postings.JobPosting', on_delete = models.CASCADE)

    class Meta:
        db_table = 'reads'