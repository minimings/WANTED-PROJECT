from django.db import models

class Suggestion(models.Model):
    is_suggestion = models.BooleanField(default = False)
    general_user  = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    company       = models.ForeignKey('postings.Company', on_delete = models.CASCADE)

    class Meta:
        db_table = 'suggestions'