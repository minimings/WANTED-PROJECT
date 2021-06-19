from django.db import models

class CountryCode(models.Model):
    code = models.CharField(max_length = 45)

    class Meta:
        db_table = 'country_codes'