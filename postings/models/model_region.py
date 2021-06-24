from django.db import models

class Region(models.Model):
    name   = models.CharField(max_length = 45)
    nation = models.ForeignKey('postings.nation', models.SET_NULL, null = True)

    class Meta:
        db_table = 'regions'