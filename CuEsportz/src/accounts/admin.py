from django.contrib import admin
from accounts.models import UserDetail, UserPassword

# Register your models here.
from django.contrib.sessions.models import Session
Session.objects.all().delete()
admin.site.register(UserDetail)
admin.site.register(UserPassword)