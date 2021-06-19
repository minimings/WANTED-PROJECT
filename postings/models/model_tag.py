from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'tags'

class CompanyTag(models.Model):
    company = models.ForeignKey('postings.Company', on_delete = models.CASCADE)
    tag     = models.ForeignKey('postings.Tag', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'company_tags'