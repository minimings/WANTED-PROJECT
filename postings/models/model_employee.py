from django.db import models

class Employee(models.Model):
    employee = models.CharField(max_length = 45)

    class Meta:
        db_table = 'employees'