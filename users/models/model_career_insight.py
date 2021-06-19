from django.db import models

class CareerInsight(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'career_insights'

class UserCareerInsight(models.Model):
    general_user   = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    career_insight = models.ForeignKey('users.CareerInsight', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_career_insights'