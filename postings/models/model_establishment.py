from django.db import models

class Establishment(models.Model):
    establishment = models.CharField(max_length = 45)

    class Meta:
        db_table = 'establishments'