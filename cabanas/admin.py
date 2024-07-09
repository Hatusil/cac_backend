from django.contrib import admin

# Register your models here.
from .models import ContactForm

admin.site.register(ContactForm)
# cabanas/models.py
from django.db import models
from .admin import admin  # This will cause a circular import error