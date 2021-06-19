from django.db import models

class LanguageExam(models.Model):
    name  = models.CharField(max_length = 45)
    grade = models.CharField(max_length = 45)
    date  = models.DateTimeField()

    class Meta:
        db_table = 'language_exams'