from django.db import models

class LanguageLevel(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'language_levels'