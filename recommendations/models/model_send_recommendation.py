from recommendations.models.model_relation import Relation
from django.db import models

class SendRecommendation(models.Model):
    name         = models.CharField(max_length = 45)
    phone_number = models.IntegerField()
    country_code = models.ForeignKey('users.CountryCode', on_delete = models.SET_NULL, null = True)
    relation     = models.ForeignKey('recommendations.Relation', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'send_recommendations'