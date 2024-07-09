from django.db import models

# Create your models here.

class ContactFormModel(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    guests = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()

