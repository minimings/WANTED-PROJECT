from django.db import models

class ProfileImage(models.Model):
    profile_image = models.URLField(max_length = 2000)

    class Meta:
        db_table = 'profile_images'