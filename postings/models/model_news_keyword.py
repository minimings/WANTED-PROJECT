from django.db import models

class NewsKeyword(models.Model):
    keyword = models.CharField(max_length = 45)

    class Meta:
        db_table = 'news_keywords'


class CompanyNewsKeyword(models.Model):
    company      = models.ForeignKey('postings.Company', on_delete = models.CASCADE)
    news_keyword = models.ForeignKey('postings.NewsKeyword', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'company_news_keywords'