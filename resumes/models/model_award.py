from django.db import models

class Award(models.Model):
    date         = models.DateTimeField()
    title        = models.CharField(max_length = 45)
    description  = models.CharField(max_length = 2000)
    write_resume = models.ForeignKey('resumes.WriteResume', on_delete = models.CASCADE)

    class Meate:
        db_table = 'awards'