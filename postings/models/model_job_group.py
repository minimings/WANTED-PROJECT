from django.db import models

class JobGroup(models.Model):
    name = models.CharField(max_length = 45)
    menu = models.ForeignKey('postings.Menu', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'job_groups'

    def __str__(self):
        return self.name