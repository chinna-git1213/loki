from django.contrib import admin
from webapp.models import UserProfile,form_email
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(form_email)

