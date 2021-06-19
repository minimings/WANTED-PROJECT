from django.db import models

class MajorAchievement(models.Model):
    start_date      = models.DateTimeField()
    end_date        = models.DateTimeField()
    title           = models.CharField(max_length = 45)
    description     = models.CharField(max_length = 1000)
    work_experience = models.ForeignKey('resumes.WorkExperience', on_delete = models.CASCADE)

    class Meta:
        db_table = 'major_achievements'