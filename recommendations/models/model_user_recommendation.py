from django.db import models

class UserRecommendation(models.Model):
    send_user      = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE, related_name = 'send_user')
    reception_user = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE, related_name = 'reception_user')

    class Meta:
        db_table = 'user_recommendations'