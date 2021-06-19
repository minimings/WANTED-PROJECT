from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'skills'

class UserSkill(models.Model):
    general_user = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    skill        = models.ForeignKey('users.Skill', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_skills'