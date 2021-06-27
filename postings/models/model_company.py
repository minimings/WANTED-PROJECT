from django.db import models

from tinymce import HTMLField

class Company(models.Model):
    name                        = models.CharField(max_length = 45)
    address                     = models.CharField(max_length = 500, null = True)
    company_registration_number = models.IntegerField(null = True)
    investment_amount           = models.IntegerField(null = True)
    description                 = HTMLField(null = True)
    subscription_path           = models.CharField(max_length = 45, null = True)
    is_mainview                 = models.BooleanField(default = False)
    longitude                   = models.DecimalField(max_digits = 26, decimal_places = 20, null = True)
    latitude                    = models.DecimalField(max_digits = 26, decimal_places = 20, null = True)
    nation                      = models.ForeignKey('postings.Nation', on_delete = models.SET_NULL, null = True)
    region                      = models.ForeignKey('postings.Region', on_delete = models.SET_NULL, null = True)
    employees                   = models.ForeignKey('postings.Employee', models.SET_NULL, null = True)
    job_group                   = models.ForeignKey('postings.JobGroup', models.SET_NULL, null = True)
    establishment               = models.ForeignKey('postings.Establishment', models.SET_NULL, null = True)
    company_news_keyword        = models.ManyToManyField('postings.NewsKeyword', through = 'postings.CompanyNewsKeyword')
    company_information         = models.ManyToManyField('postings.CompanyInformation', through = 'postings.CompanyInformationDate')
    tag                         = models.ManyToManyField('postings.Tag', through = 'postings.CompanyTag')
    icon                        = models.OneToOneField('postings.Icon', on_delete = models.SET_NULL, null = True)
    company_user                = models.OneToOneField('users.CompanyUser', on_delete = models.CASCADE, null = True)
    created_at                  = models.DateTimeField(auto_now_add = True)
    updated_at                  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name