from django.db import models

class University(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'university'


class UserUniversity(models.Model):
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    is_enrolled = models.BooleanField()
    major       = models.CharField(max_length = 45)
    description = models.CharField(max_length = 1000)

    class Meta:
        db_table = 'user_university'