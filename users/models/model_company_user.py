from django.db import models

class CompanyUser(models.Model):
    position = models.CharField(max_length = 45)
    user     = models.ForeignKey('users.User', on_delete = models.CASCADE)

    class Meta:
        db_table = 'company_users'