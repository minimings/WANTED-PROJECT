from django.db import models

class ForeignLanguage(models.Model):
    language       = models.ForeignKey('resumes.Language', on_delete = models.SET_NULL, null = True)
    language_level = models.ForeignKey('resumes.LanguageLevel', on_delete = models.SET_NULL, null = True)
    language_exam  = models.ForeignKey('resumes.LanguageExam', on_delete = models.SET_NULL, null = True)
    write_resume   = models.ForeignKey('resumes.WriteResume', on_delete = models.CASCADE)

    class Meta:
        db_table = 'foreign_languages'