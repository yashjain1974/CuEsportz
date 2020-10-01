# importing necessary files
from django.contrib import admin
from accounts.models import UserDetail, UserPassword
from django.contrib.sessions.models import Session

# registering models for admin
admin.site.register(UserDetail)
admin.site.register(UserPassword)

# deleting undetected sessions
Session.objects.all().delete()
