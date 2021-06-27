from django.db import models

class Nation(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'nations'

    def __str__(self):
        return self.name