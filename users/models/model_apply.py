from django.db import models

class Apply(models.Model):
    general_user  = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    job_posting   = models.ForeignKey('postings.JobPosting', on_delete = models.CASCADE)
    apply_status  = models.ForeignKey('users.ApplyStatus', on_delete = models.SET_NULL, null = True)
    reward_status = models.ForeignKey('users.RewardStatus', on_delete = models.SET_NULL, null = True)
    created_at    = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'apply'