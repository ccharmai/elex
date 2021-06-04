from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.Maker)
admin.site.register(models.Type)
admin.site.register(models.Item)
admin.site.register(models.Modification)
admin.site.register(models.Property)
admin.site.register(models.Log)
