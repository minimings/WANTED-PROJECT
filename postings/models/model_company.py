from django.db import models
from django.db.models.fields import URLField

class Company(models.Model):
    name                        = models.CharField(max_length = 45)
    address                     = models.CharField(max_length = 500)
    company_registration_number = models.IntegerField()
    investment_amount           = models.IntegerField()
    description                 = models.TextField()
    website_address             = models.CharField(max_length = 500, null = True)
    subscription_path           = models.CharField(max_length = 45, null = True)
    nation                      = models.ForeignKey('postings.Nation', on_delete = models.SET_NULL, null = True)
    region                      = models.ForeignKey('postings.Region', on_delete = models.SET_NULL, null = True)
    employees                   = models.ForeignKey('postings.Employee', models.SET_NULL, null = True)
    job_group                   = models.ForeignKey('postings.JobGroup', models.SET_NULL, null = True)
    news_keyword                = models.ManyToManyField('postings.NewsKeyword', through = 'postings.CompanyNewsKeyword')
    company_information         = models.ManyToManyField('postings.CompanyInformation', through = 'postings.CompanyInformationDate')
    tag                         = models.ManyToManyField('postings.Tag', through = 'postings.CompanyTag')
    icon                        = models.OneToOneField('postings.Icon', on_delete = models.SET_NULL, null = True)
    company_user                = models.OneToOneField('users.CompanyUser', on_delete = models.CASCADE)

    class Meta:
        db_table = 'company'