from django.db import models

class JobPostingImage(models.Model):
    job_posting_image = models.FileField(max_length = 2000)
    job_posting       = models.ForeignKey('postings.JobPosting', on_delete = models.CASCADE)

    class Meta:
        db_table = 'job_posting_images'

    def __str__(self):
        return str(self.job_posting_image)