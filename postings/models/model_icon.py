from django.db import models

class Icon(models.Model):
    icon = models.FileField(max_length = 2000)

    class Meta:
        db_table = 'icon'

    def __str__(self):
        return str(self.icon)