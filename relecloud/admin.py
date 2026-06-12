# pyrefly: ignore [missing-import]
from relecloud import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.Destination)
admin.site.register(models.Cruise)
admin.site.register(models.InfoRequest)
