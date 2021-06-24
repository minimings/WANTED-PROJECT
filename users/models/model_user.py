from django.db                  import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fileds):
        if not email:
            raise ValueError('must have user email')

        user = self.model(
            email = self.normalize_email(email),
            **extra_fileds,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password = None, **extra_fileds):
        user = self.create_user(
            email = self.normalize_email(email),
            **extra_fileds,
        )

        user.is_superuser = True
        user.is_staff     = True
        user.set_password(password)
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_GENERAL_USER = '일반회원'
    USER_TYPE_COMPANY_USER = '기업회원'

    USER_TYPES = (
        (USER_TYPE_GENERAL_USER, '일반회원'),
        (USER_TYPE_COMPANY_USER, '기업회원'),
    )

    email         = models.EmailField(max_length = 45, unique = True)
    name          = models.CharField(max_length = 45)
    phone_number  = models.IntegerField(null = True)
    password      = models.CharField(max_length = 500)
    is_social     = models.BooleanField(default = False)
    type          = models.CharField(max_length = 45, choices = USER_TYPES)
    kakao_user_id = models.IntegerField(null = True)
    is_staff      = models.BooleanField(default = False)
    is_active     = models.BooleanField(default = True)
    country_code  = models.ForeignKey('users.CountryCode', on_delete = models.SET_NULL, null = True)
    social        = models.ForeignKey('users.Social', on_delete = models.SET_NULL, null = True)
    
    objects = UserManager()

    USERNAME_FIELD  = 'email'

    class Meta:
        db_table  = 'users'
        swappable = 'AUTH_USER_MODEL'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True