from django.contrib             import admin
from django.contrib.auth.models import User

from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display      = ['name', 'email', 'phone_number']
    list_display_link = ['name']

admin.site.register(User, UserAdmin)