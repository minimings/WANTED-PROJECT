from users.models.model_worry import Worry
from django.db import models

class InterestedKeyword(models.Model):
    name  = models.CharField(max_length = 45)
    worry = models.ForeignKey('users.Worry', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'interested_keywords'

class UserInterestedKeyword(models.Model):
    general_user       = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    interested_keyword = models.ForeignKey('users.InterestedKeyword', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_interested_keywords'