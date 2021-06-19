from django.db import models

class Network(models.Model):
    major        = models.CharField(max_length = 45)
    is_disclosed = models.BooleanField(default = True)
    university   = models.ForeignKey('users.University', on_delete = models.SET_NULL, null = True)
    company      = models.ForeignKey('postings.Company', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'networks'