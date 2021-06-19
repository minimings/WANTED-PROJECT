from django.db import models

class PhoneCheck(models.Model):
    phone_number = models.CharField(max_length = 45)
    auth_number  = models.CharField(max_length = 45)

    class Meta:
        db_table = 'phone_checks'