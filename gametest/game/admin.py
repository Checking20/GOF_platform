from django.contrib import admin
from game import models
# Register your models here.
admin.site.register(models.GUser)
admin.site.register(models.GMap)
admin.site.register(models.State)
admin.site.register(models.Comment)