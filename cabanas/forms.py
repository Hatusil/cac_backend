from django import forms
from .models import Contact, ContactFormModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = '__all__'