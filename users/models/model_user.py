from django.db import models

class User(models.Model):
    USER_TYPE_GENERAL_USER = '일반회원'
    USER_TYPE_COMPANY_USER = '기업회원'

    USER_TYPES = (
        (USER_TYPE_GENERAL_USER, '일반회원'),
        (USER_TYPE_COMPANY_USER, '기업회원'),
    )

    email         = models.EmailField(max_length = 45)
    name          = models.CharField(max_length = 45)
    phone_number  = models.IntegerField
    password      = models.CharField(max_length = 500)
    is_social     = models.BooleanField(default = False)
    type          = models.CharField(max_length = 45)
    country_code  = models.ForeignKey('users.CountryCode', on_delete = models.SET_NULL, null = True)
    social        = models.ForeignKey('users.Social', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'users'