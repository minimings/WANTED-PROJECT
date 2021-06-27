from django.db import models

class GeneralUser(models.Model):
    is_subscribe       = models.BooleanField(default = False)
    career             = models.ForeignKey('users.Career', on_delete = models.SET_NULL, null = True)
    job_group          = models.ForeignKey('postings.JobGroup', on_delete = models.SET_NULL, null = True)
    worry              = models.ForeignKey('users.Worry', on_delete = models.SET_NULL, null = True)
    profile_image      = models.OneToOneField('users.ProfileImage', on_delete = models.SET_NULL, null = True)
    user               = models.OneToOneField('users.User', on_delete = models.CASCADE)
    skill              = models.ManyToManyField('users.Skill', through = 'users.UserSkill')
    interested_keyword = models.ManyToManyField('users.InterestedKeyword', through = 'users.UserInterestedKeyword')
    user_university    = models.ManyToManyField('users.University', through = 'users.UserUniversity')
    user_company       = models.ManyToManyField('postings.Company', through = 'users.UserCompany')

    class Meta:
        db_table = 'general_users'

    def __str__(self):
        return self.user.name

class Follow(models.Model):
    is_follow    = models.BooleanField(default = False)
    general_user = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    company      = models.ForeignKey('postings.Company', on_delete = models.CASCADE)

    class Meta:
        db_table = 'follows'

class UserCompany(models.Model):
    general_user = models.ForeignKey('users.GeneralUser', on_delete = models.CASCADE)
    company      = models.ForeignKey('postings.Company', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_company'