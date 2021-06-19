from django.db import models

class JobPostingImage(models.Model):
    job_posting_image = models.URLField(max_length = 2000)
    job_posting       = models.ForeignKey('postings.JobPostingImage', on_delete = models.CASCADE)

    class Meta:
        db_table = 'job_posting_images'