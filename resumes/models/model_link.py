from django.db import models

class Link(models.Model):
    link         = models.URLField(max_length = 2000)
    write_resume = models.ForeignKey('resumes.WriteResume', on_delete = models.CASCADE)

    class Meta:
        db_table = 'links'