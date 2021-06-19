from django.db import models

class Icon(models.Model):
    icon = models.URLField(max_length = 2000)

    class Meta:
        db_table = 'icon'