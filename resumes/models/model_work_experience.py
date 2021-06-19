from django.db import models

class WorkExperience(models.Model):
    start_date   = models.DateTimeField()
    end_date     = models.DateTimeField(null = True)
    is_working   = models.BooleanField(default = False)
    position     = models.CharField(max_length = 45)
    company      = models.ForeignKey('postings.Company', on_delete = models.SET_NULL, null = True)
    write_resume = models.ForeignKey('resumes.WriteResume', on_delete = models.CASCADE)

    class Meta:
        db_table = 'work_experiences'