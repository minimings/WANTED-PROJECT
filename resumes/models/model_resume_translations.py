from django.db import models

class ResumeTranslation(models.Model):
    write_resume = models.ForeignKey('resumes.WriteResume', on_delete = models.CASCADE)
    translation  = models.ForeignKey('resumes.Translation', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'resume_translations'