from django.db import models

class Career(models.Model):
    career = models.CharField(max_length = 45)

    class Meta:
        db_table = 'careers'

    def __str__(self):
        return self.career