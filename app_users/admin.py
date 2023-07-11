from django.contrib import admin
from django.contrib.auth.models import User
from app_users.models import UserProfile


class ShowUser(admin.AdminSite):
    model = User
    fields = ['user', 'firstname', 'lastname', 'email']


admin.site.register(UserProfile)

