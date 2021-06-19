from django.db import models

class CompleteStatus(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'complete_status'