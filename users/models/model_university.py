from django.db import models

class University(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'university'


class UserUniversity(models.Model):
    start_date   = models.DateTimeField(null = True)
    end_date     = models.DateTimeField(null = True)
    is_enrolled  = models.BooleanField(default = False)
    major        = models.CharField(max_length = 45, null = True)
    description  = models.CharField(max_length = 1000, null = True)
    general_user = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    university   = models.ForeignKey('users.University', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_university'