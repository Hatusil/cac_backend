from django.contrib import admin

# Register your models here.
from .models import ContactFormModel

admin.site.register(ContactFormModel)
# cabanas/models.py
from django.db import models
from .admin import admin  # This will cause a circular import error