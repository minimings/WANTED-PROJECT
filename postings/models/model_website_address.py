from django.db import models

class WebsiteAddress(models.Model):
    website_address = models.CharField(max_length = 500)
    company         = models.ForeignKey('postings.Company', models.CASCADE)

    class Meta:
        db_table = 'website_address'