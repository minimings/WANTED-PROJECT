from django.db import models

class JobCompetency(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'job_competency'

class UserJobCompetency(models.Model):
    general_user   = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    job_competency = models.ForeignKey('users.JobCompetency', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_job_competency'