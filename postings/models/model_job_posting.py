from django.db import models

class JobPosting(models.Model):
    title       = models.CharField(max_length = 45)
    longitute   = models.CharField(max_length = 45)
    latitude    = models.CharField(max_length = 45)
    description = models.TextField()
    deadline    = models.DateTimeField()
    company     = models.ForeignKey('postings.Company', on_delete = models.CASCADE)

    class Meta:
        db_table = 'job_postings'