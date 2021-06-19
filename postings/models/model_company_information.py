from django.db import models
from django.db.models.deletion import SET_NULL

class CompanyInformation(models.Model):
    newcomer_salary = models.IntegerField()
    average_salary  = models.IntegerField()
    total_employee  = models.IntegerField()

    class Meta:
        db_table = 'company_informations'


class CompanyInformationDate(models.Model):
    entrant             = models.IntegerField()
    retiree             = models.IntegerField()
    company             = models.ForeignKey('postings.Company', on_delete = models.CASCADE)
    company_information = models.ForeignKey('postings.CompanyInformation', on_delete = SET_NULL, null = True)
    date                = models.DateTimeField()

    class Meta:
        db_table = 'company_information_dates'