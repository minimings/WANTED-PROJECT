from django.db import models

class RewardStatus(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'reward_status'