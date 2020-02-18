from django.contrib import admin

# Register your models here.
from .models import Users, Notes, Notifications

admin.site.register(Users)
admin.site.register(Notes)
admin.site.register(Notifications)
