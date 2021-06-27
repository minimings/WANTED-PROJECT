from django.db import models

from tinymce.models import HTMLField

class JobPosting(models.Model):
    title       = models.CharField(max_length = 45)
    description = HTMLField()
    deadline    = models.DateTimeField()
    company     = models.ForeignKey('postings.Company', on_delete = models.CASCADE)

    class Meta:
        db_table = 'job_postings'

    def __str__(self):
        return self.title