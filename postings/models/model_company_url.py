from django.db import models

class CompanyImage(models.Model):
    company_image = models.CharField(max_length = 2000)
    company       = models.ForeignKey('postings.Company', on_delete = models.CASCADE)

    class Meta:
        db_table = 'company_images'