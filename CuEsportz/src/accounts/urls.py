from django.urls import path
from . import views
from django.contrib import admin

# Customizing django admin site
admin.site.site_header = "CuEsportz Admins"
admin.site.site_title = "Admin log in here"
admin.site.index_title = "welcome Admins" 

urlpatterns = [
    path('', views.registration, name="registeration"),
    path('signin', views.signIn, name="signin"),
    path('signup', views.signUp, name="signup"),
    path('join', views.joinPage, name="join"),
    path('wallet', views.walletPage, name="wallet"),
]
