from webbrowser import register

from django.contrib import admin
from django.contrib.auth.models import User

from appTwo.models import User

# Register your models here.


admin.site.register(User)
